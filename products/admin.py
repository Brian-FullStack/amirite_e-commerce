'''
Necessary Imports
'''
from django.contrib import admin
from .models import Product, Category

# Register Product and Catregory models
admin.site.register(Product)
admin.site.register(Category)
