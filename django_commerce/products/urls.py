from django.urls import path
from . views import Home, ProductDetail
from . import views


from django.conf import settings
from django.conf.urls.static import static

from cart.views import add_to_cart, remove_from_cart, CartView, decreaseCart


app_name = 'mainapp'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cart/', CartView, name='cart-home'),
    path('cart/<slug>/', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
    path('decrease-cart/<slug>', decreaseCart, name='decrease-cart'),
    path('detail/<slug>/', ProductDetail.as_view(), name='detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)