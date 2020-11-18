import re
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from decimal import *
from datetime import datetime
from xero import Xero
from xero.auth import PrivateCredentials
from carts.models import Cart, CartItem
from shipping.models import Suburb
from xero_app.utils import account_code_selector

XERO_RSA_KEY = getattr(settings, "XERO_RSA_KEY", 'error')
XERO_CONSUMER_KEY = getattr(settings, "XERO_CONSUMER_KEY", 'error')
XERO_SECRET_KEY = getattr(settings, 'XERO_SECRET_KEY', 'error')

def stateSupplierTitle(customerState, item):
    if customerState == 'NSW' or customerState == 'ACT' and item.product.nsw_supplier_title != None:
        if hasattr(item.product, 'nsw_supplier_title'):
            return item.product.nsw_supplier_title
        else: 
            return item.product.title
    elif customerState == 'WA' and item.product.wa_supplier_title != None:
        if hasattr(item.product, 'wa_supplier_title'):
            return item.product.wa_supplier_title
        else: 
            return item.product.title
    elif customerState == 'QLD' and item.product.qld_supplier_title != None:
        if hasattr(item.product, 'qld_supplier_title'):
            return item.product.qld_supplier_title
        else: 
            return item.product.title
    else:
        if hasattr(item.product, 'vic_supplier_title') and item.product.vic_supplier_title != None:
            return item.product.vic_supplier_title
        else: 
            return item.product.title
    
    return item.product.title

def cart_invoice_create(request):
    name = request.POST.get('name')
    phone_number = request.POST.get('phone_number')
    email = request.POST.get('email')
    pickup = request.POST.get('pickup')
    postage_standard = request.POST.get('postage_standard')
    postage_express = request.POST.get('postage_express')
    address = request.POST.get('address')
    suburb = request.POST.get('suburb')
    postcode = request.POST.get('postcode')
    state = request.POST.get('state')
    billing_address = request.POST.get('billing_address')
    billing_suburb = request.POST.get('billing_suburb')
    billing_postcode = request.POST.get('billing_postcode')
    billing_state = request.POST.get('billing_state')
    billing_same = request.POST.get('billing_same')
    pk = request.POST.get('pk')
    shipping_price = 0

    # If not pickup, add price
    if address != '48 Watt Rd':
        try:
            shipping = Suburb.objects.filter(postal_code=postcode).first()
            shipping_price = shipping.delivery_price
        except:
            pass

    try:
        cart_obj = Cart.objects.get(pk=pk)
    except:
        print("ERROR CART")
        data = {
            'error': 'Cart no longer exists'
        }
        return JsonResponse(data, status=500)

    with open(XERO_RSA_KEY) as keyfile:
        rsa_key = keyfile.read()
    consumer_key = XERO_CONSUMER_KEY
    consumer_secret = XERO_SECRET_KEY
    credentials = PrivateCredentials(consumer_key, rsa_key)
    xero = Xero(credentials)
    time = datetime.now()

    invoice = {
        "Type": "ACCREC",
        "CurrencyCode": "AUD",
        "Contact": 
            {
                "Name": str(name) + " - " + str(phone_number),
                "EmailAddress": str(email),
                "Addresses": [{
                    "AddressType": "STREET",
                    "AddressLine1": str(billing_address) + ", " + str(billing_state),
                    "City": str(billing_suburb),
                    "PostalCade": str(billing_postcode),
                }]
            },
        "Date": datetime(time.year, time.month, time.day),
        "DueDate": datetime(time.year, time.month, time.day),
        "LineAmountTypes": "Inclusive",
        "LineItems": [
            {
                "Description": re.sub('[®]', '', stateSupplierTitle(state, item)) + "\n" \
                    + ("Colour: " + item.colour.colour + "\n" if item.colour else "") \
                    + ("Length: " + str(item.length) + "\n" if item.length else "") \
                    + ("Additional: " + item.additional_drop_down.title if item.additional_drop_down else ""),
                "Quantity": item.quantity,
                "UnitAmount": str(round(Decimal(item.price), 2)),
                "AccountCode": account_code_selector(item, state),
                "TaxType": "OUTPUT",
            } for item in cart_obj.cartitem_set.all()
        ],
        "Status": "AUTHORISED",
    }


    if postage_express == 'true':
        invoice['LineItems'].append(
            {
                "Description": "Shipping: " + str(address) + ", " + str(suburb) + ", " + str(postcode) + ", " + str(state),
                "Quantity": "1",
                "UnitAmount": str(Decimal(25.99)),
                "TaxType": "OUTPUT",
                "AccountCode": "654"
            }
        )
    elif postage_standard == 'true':
        invoice['LineItems'].append(
            {
                "Description": "Shipping: " + str(address) + ", " + str(suburb) + ", " + str(postcode) + ", " + str(state),
                "Quantity": "1",
                "UnitAmount": str(Decimal(17.99)),
                "TaxType": "OUTPUT",
                "AccountCode": "654"
            }
        )
    elif shipping_price > 0:
        invoice['LineItems'].append(
            {
                "Description": "Shipping: " + str(address) + ", " + str(suburb) + ", " + str(postcode) + ", " + str(state),
                "Quantity": "1",
                "UnitAmount": str(Decimal(shipping_price)),
                "TaxType": "OUTPUT",
                "AccountCode": "654"
            }
        )
    elif address == "48 Watt Rd":
        invoice['LineItems'].append(
            {
                "Description": "Pickup: " + str(address) + ", " + str(suburb) + ", " + str(postcode) + ", " + str(state),
                "Quantity": "1",
                "UnitAmount": "0",
                "TaxType": "OUTPUT",
                "AccountCode": "654"
            }
        )
    else:
        invoice['LineItems'].append(
            {
                "Description": "Shipping To Undefined Postcode: " + str(address) + ", " + str(suburb) + ", " + str(postcode) + ", " + str(state),
                "Quantity": "1",
                "UnitAmount": "0",
                "TaxType": "OUTPUT",
                "AccountCode": "654"
            }
        )

    new_invoice = xero.invoices.put(invoice)

    data = {
        'success': 'success'
    }

    return JsonResponse(data)