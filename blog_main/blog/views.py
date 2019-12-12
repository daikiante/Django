from django.shortcuts import render
from .models import Category, Post

def index(request):
    return render(request,'blog/index.html')

def blog(request):
    contents = Post.objects.all().order_by('-create_on')
    return render(request, 'blog/blog.html', {'contents': contents})

def category(request):
    posts = Post.objects.fillter(categories__name__contains=category).order_by('-created_on')
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'blog/blog.html', context)