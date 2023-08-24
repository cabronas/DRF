from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2)
    count = models.IntegerField()
    comment = models.CharField(max_length=50)
