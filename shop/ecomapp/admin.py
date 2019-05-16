from django.contrib import admin

# Register your models here.
from ecomapp.models import Category
from ecomapp.models import Brand
from ecomapp.models import Product

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
