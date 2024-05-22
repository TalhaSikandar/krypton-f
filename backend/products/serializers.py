
from rest_framework import serializers
from .models import Product, ProductRawmaterial
from raw_materials.serializers import RawmaterialSerializer

class ProductRawmaterialSerializer(serializers.ModelSerializer):
    raw_material = RawmaterialSerializer()
    class Meta:
        model = ProductRawmaterial
        fields = ['id', 'product', 'raw_material', ]

class ProductSerializer(serializers.ModelSerializer):
    raw_materials = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'raw_materials', 'updated_at', ]

