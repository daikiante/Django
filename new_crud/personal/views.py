from django.shortcuts import render
from django.shortcuts import redirect
from . forms import ALLInfoForm

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

def create_info(request):
    form = ALLInfoForm(request.POST or None)
    # is_valid() = it check for all values
    if form.is_valid():
        form.save()
        return redirect(home)

    return render(request, 'all-info-form.html',{'form':form})