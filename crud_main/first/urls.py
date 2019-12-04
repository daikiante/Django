from django.urls import path
from . import views


urlpatterns = [
    path('lohit', views.home),
    path('about', views.about),
    path('fixed', views.fixed),
    path('practice', views.practice)
]
