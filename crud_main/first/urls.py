from django.urls import path
from . import views


urlpatterns = [
    path('lohit', views.home),
    path('about', views.about)
]
