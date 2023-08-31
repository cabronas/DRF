from django.contrib.auth.models import User
from django.db import models
# from djoser.conf import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    count = models.IntegerField()
    comment = models.CharField(max_length=50)
    visible = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
