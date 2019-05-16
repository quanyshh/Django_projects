from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    contex = {
        'categories': categories,
        'products': products
    }
    return render(request, 'index.html', contex)
