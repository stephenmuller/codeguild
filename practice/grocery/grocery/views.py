"""grocery Views."""

from .logic import convert_currency
from .logic import lookup_product_for_name
from django.http import HttpResponse
from .models import PRODUCTS, EXCHANGERATE


def get_product(request, product_name):
    try:
        price_dollars = lookup_product_for_name(product_name)['price_dollars']
    except KeyError:
        return HttpResponse('this product is fake, try again', status=404)
    response_str = 'One {} is ${}'.format(product_name, price_dollars)
    return HttpResponse(response_str)


def get_product_currency(request, product_name, currency):
    try:
        price_dollars = lookup_product_for_name(product_name)['price_dollars']
    except KeyError:
        return HttpResponse('this product is fake, try again', status=404)
    try:
        price_new_currency = convert_currency(price_dollars, 'dollars', currency)
    except ValueError:
        return HttpResponse('this currency is wrong, try again', status=404)
    response_str = 'Price for {} is {} {}'.format(product_name, price_new_currency, currency)
    return HttpResponse(response_str)
