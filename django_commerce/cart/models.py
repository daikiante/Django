from django.db import models

from django.contrib.auth import get_user_model

# .modelsだと同じ階層になってしまう。productsフォルダから呼び出すにはproducts.modelsとする。
from products.models import Product


User = get_user_model()

class Cart(models.Model):
    # Userとつなげる
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # プロダクトとつなげる
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

    # カウントするためのフィールド
    quantity = models.IntegerField(default=1)

    # 作った時間
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

    def get_total(self):
        return self.item.price * self.quantity


class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += order_item.get_total()

        return total