from django.shortcuts import render
from django.http import JsonResponse

from shipping.models import Suburb

# Ajax get postcode price
def get_postcode_price(request):

    post_code = request.POST.get('post_code', None)
    postage = request.POST.get('postage', None)
    price = 0
    location = request.session.setdefault('state_selected', 'VIC')
    try:
        postcode_obj = Suburb.objects.get(postal_code=int(post_code))
    except:
        postcode_obj = None

    if postage == 'true':
        if location =='VIC':
            post_code = 'You can pick this product up from our Mornington location for free. <br> Standard ($17.99) and Express Shipping ($25.99) apply to this product!'
        else:
            post_code = 'Standard ($17.99) and Express Shipping ($25.99) apply to this product!'
    elif post_code and postcode_obj:
        if postcode_obj.delivery_price > 0:
            if location == 'VIC':
                post_code = 'You can pick this product up from our Mornington location for free. <br> Shipping to postal code: ' + str(postcode_obj.postal_code) + " is $" + str(postcode_obj.delivery_price)
            else:
                post_code = 'Shipping to postal code: ' + str(postcode_obj.postal_code) + " is $" + str(postcode_obj.delivery_price)
        else:
            post_code = "Please contact us for a delivery price."
    else:
        post_code = "Please contact us for a delivery price."

    
    data = {
        "post_code": post_code
    }

    return JsonResponse(data)