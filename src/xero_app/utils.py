import re

from django.conf import settings
from django.utils import timezone

from decimal import *
from datetime import datetime

from xero import Xero
from xero.auth import PrivateCredentials

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

def account_code_selector(item, state_selected):

    # Check if the product is a flashing
    flashings = False
    for category in item.product.categoryoption_set.all():
        if category == 'Flashings':
            flashings = True
            break

    if state_selected == 'VIC' and flashings:
        return "239"
    elif state_selected == 'ACT':
        return "NSW"
    elif state_selected == 'NSW':
        return "NSW"
    elif state_selected == 'NT':
        return "NT"
    elif state_selected == 'QLD':
        return "QLD"
    elif state_selected == 'SA':
        return "SA"
    elif state_selected == 'TAS':
        return "TAS"
    elif state_selected == 'VIC':
        return "VIC"
    elif state_selected == 'WA':
        return "WA"

    return

def get_account_code(order_obj):
    if order_obj.payment_type == 'PayPal' or order_obj.payment_type == 'Paypal':
        return '120'

    return 'STRIPE'

def xero_invoice(order_obj, state_selected):
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
                "Name": str(order_obj.shipping_address.get_name()) + " " + str(order_obj.shipping_address.phone_number),
                "EmailAddress": str(order_obj.billing_profile.email)
            },
        "Date": datetime(time.year, time.month, time.day),
        "DueDate": datetime(time.year, time.month, time.day),
        "LineAmountTypes": "Inclusive",
        "LineItems": [
            {
                "Description": re.sub('[®]', '', stateSupplierTitle(state_selected, item)) + "\n" \
                    + ("Colour: " + item.colour.colour + "\n" if item.colour else "") \
                    + ("Length: " + str(item.length) + "\n" if item.length else "") \
                    + ("Additional: " + item.additional_drop_down.title if item.additional_drop_down else ""),
                "Quantity": item.quantity,
                "UnitAmount": str(round(Decimal(item.price), 2)),
                "AccountCode": account_code_selector(item, state_selected),
                "TaxType": "OUTPUT",
            } for item in order_obj.orderitem_set.all()
        ],
        "Status": "AUTHORISED",
    }

    # Add shipping cost to invoice
    if order_obj.shipping_total > 0:
        invoice['LineItems'].append(
            {
                "Description": "Shipping: " + str(order_obj.shipping_address.get_address()),
                "Quantity": "1",
                "TaxType": "OUTPUT",
                "UnitAmount": str(round(Decimal(order_obj.shipping_total), 2)),
                "AccountCode": "654"
            }
        )
    
    new_invoice = xero.invoices.put(invoice)

    return new_invoice


def xero_payment(order_obj, new_invoice):
    with open(XERO_RSA_KEY) as keyfile:
        rsa_key = keyfile.read()
    consumer_key = XERO_CONSUMER_KEY
    consumer_secret = XERO_SECRET_KEY
    credentials = PrivateCredentials(consumer_key, rsa_key)
    xero = Xero(credentials)
    time = datetime.now()

    invoiceID = new_invoice[0]['InvoiceID']
    invoice = xero.invoices.get(invoiceID)
                

    payment = {
        "Invoice": {"InvoiceID": invoiceID},
        "Account": {"Code": get_account_code(order_obj)},
        "Date": datetime(time.year, time.month, time.day, time.hour, time.minute),
        "Amount": str(invoice[0]['Total']),
    }

    new_payment = xero.payments.put(payment)

    return new_payment