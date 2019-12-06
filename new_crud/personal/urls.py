
from django.urls import path
from . import views

urlpatterns = [
   path('home/', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('create', views.create_info, name='create_info')
]
