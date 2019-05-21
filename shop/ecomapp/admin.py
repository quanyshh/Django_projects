from django.contrib import admin

# Register your models here.
from ecomapp.models import Category, Brand, Product, Discount, CartItem, Cart, Order

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)
