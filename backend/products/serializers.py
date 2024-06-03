
from rest_framework import serializers
from .models import Product, ProductRawmaterial
from raw_materials.serializers import RawmaterialSerializer

class ProductRawmaterialSerializer(serializers.ModelSerializer):
    raw_material = RawmaterialSerializer(many=True)
    class Meta:
        model = ProductRawmaterial
        fields = ['id', 'product', 'raw_material', 'unit_weight', 'required_quantity', ]

class ProductSerializer(serializers.ModelSerializer):
    raw_materials = ProductRawmaterialSerializer(required=True)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'raw_materials', 'description', 'updated_at',]

