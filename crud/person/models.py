from django.db import models

# Create your models here.

def ALLInfo(models, Model):
    
    # max_length 最大文字数
    name = models.CharField(max_length = 20)
    work = models.CharField(max_length = 20)
    experience = models.IntegerField()

    # max_digits 桁数    decimal_places 小数点
    total_salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()