from django.db import models

# Create your models here.

class Memo(models.Model):
    title = models.CharField(blank=False, null=False, max_length=30)
    text = models.TextField(blank=True, max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title