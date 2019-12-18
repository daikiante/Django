from django.contrib import admin
from django.urls import path
from .views import Home, Detail

app_name = 'products'
urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('detail', Detail.as_view(), name='detail')
]