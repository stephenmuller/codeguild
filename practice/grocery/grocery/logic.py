"""grocery Logic."""

from .models import PRODUCTS, EXCHANGERATE


def convert_currency(in_amount, in_currency, out_currency):
    """converts from the default currency (usd) to the given currency"""
    for currency in EXCHANGERATE:
        if currency['name'] == out_currency:
            return currency['rate'] * in_amount
    raise ValueError('output currency does not exist')


def lookup_product_for_name(name):
    """returns the price for a given name"""
    for product in PRODUCTS:
        if product['name'] == name:
            return product
    raise KeyError('not in the grocery list')
