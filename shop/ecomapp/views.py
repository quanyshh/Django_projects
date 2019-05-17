from django.shortcuts import render
from .models import Category, Product, Discount

# Create your views here.
def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    discounts = Discount.objects.all()
    contex = {
        'categories': categories,
        'products': products,
        'discounts': discounts
    }
    return render(request, 'ecomapp/index.html', contex)

def product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()
    contex = {
        'product' : product,
        'categories': categories
    }
    return render(request, 'ecomapp/product.html', contex)

def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    categories = Category.objects.all()
    products_of_category = Product.objects.filter(category=category)
    contex = {
        'category' : category,
        'products_of_category':products_of_category,
        'categories': categories
    }
    return render(request, 'ecomapp/category.html', contex)
