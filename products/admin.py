'''
Necessary Imports
'''
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    '''
    Tells the admin which product fields to display
    Sort products by SKU
    '''
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    '''
    Tells the admin which category fields to display
    '''
    list_display = (
        'friendly_name',
        'name',
    )


# Register Product and Catregory models and classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
