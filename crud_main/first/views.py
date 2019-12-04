from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def home(request):
    return HttpResponse('My name is Lohit')

def about(request):
    return HttpResponse('I Love Robots')