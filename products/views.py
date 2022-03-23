'''
Necessary Imports
'''
from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    '''
    Display individual product details
    '''
    # return all products from the db
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
