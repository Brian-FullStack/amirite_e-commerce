'''
Necessary Imports
'''
from django.shortcuts import render
from .models import Product


def all_products(request):
    '''
    Display all products
    '''
    # return all products from the db
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
