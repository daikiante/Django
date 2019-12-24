from django.shortcuts import render
from .models import Product, Category
from cart.models import Cart

# Create your views here.

def home(request):
    products = Product.objects.all().order_by('-id')
    context = {
        'products': products
    }
    return render(request, 'products/home.html', context)