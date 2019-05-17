from django.contrib import admin

# Register your models here.
from ecomapp.models import Category, Brand, Product, Discount

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Discount)
