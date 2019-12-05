from django.shortcuts import render

# Create your views here.

from .models import ALLInfo

def home(request):
    all_list = ALLInfo.objects.all()
    return render(request, 'home.html', {'all_list':all_list})

def about(request):
    saleryes_list = ALLInfo.objects.all()
    return render(request, 'about.html', {'saleryes_list':saleryes_list})

def contact(request):
    contact = ALLInfo.objects.all()
    return render(request, 'contact.html', {'contact':contact})