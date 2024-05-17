
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    raw_materials = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'raw_materials', 'updated_at', ]
