from django.shortcuts import render
from .models import Product
from django.views.generic import ListView

class Home(ListView):
    model = Product
    template_name = 'products/index.html'

class Detail(ListView):
    model = Product
    template_name = 'products/detail.html'