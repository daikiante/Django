from django.shortcuts import render
from .models import Product, Category
from cart.models import Cart

from django.views.generic import ListView
from products.models import Product

# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'products/home.html'