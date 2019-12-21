from django.db import models

from django.contrib.auth import get_user_model
from products.models import Product


User = get_user_model()

class Cart(models.Model):
    # Userとつなげる
    user = models.ForeignKey(user.User, on_delete=models.CASCADE)

    # プロダクトとつなげる
    item = models.ForeignKey(item.Product, on_delete=models.CASCADE)

    # カウントするためのフィールド
    quantity = models.IntegerField(default=1)

    # 作った時間
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.quantity} of {self.item.name}'