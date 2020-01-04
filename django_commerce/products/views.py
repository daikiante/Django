from django.shortcuts import render
from .models import Product, Category
from cart.models import Cart

from django.views.generic import ListView, DetailView
from products.models import Product

# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'products/home.html'
    


from django.contrib.auth.mixins import LoginRequiredMixin

class ProductDetail(LoginRequiredMixin, DetailView):
    template_name = 'products/product_detail.html'
    model = Product

'''
def product_detail(request, slug):
    item = Product.objects.get(slug=slug)
    context = {
        'item': item,
    }
    return render(request, 'products/detail.html', context)
'''