from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    count = models.IntegerField()
    comment = models.CharField(max_length=50)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'