from django.shortcuts import render

# ここから追加
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from .models import Cart, Order
from products.models import Product

def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)

    # オーダーアイテムを取得、なければ作る
    order_item, created = Cart.objects.get_or_create(
        item = item,
        user = request.user
    )

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order=order_qs[0]

    # Check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, f'{item.name} quantity has Updated')
            return redirect('mainapp:cart-home')

        else:
            order.orderitems.add(order_item)
            messages.info(request, f'{item.name} has added to your cart')
            return redirect('mainapp:cart-home')

    else:
        order = Order.objects.create(
            user=request.user
        )
        order.orderitems.add(request, f'{item.name} has added to your cart')
        return redirect('mainapp:cart-home')



