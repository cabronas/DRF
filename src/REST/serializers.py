# import serializers as serializers
from rest_framework import serializers

from REST.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'count', 'comment')
