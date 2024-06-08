
from rest_framework import serializers
# from contacts.serializers import ContactSerializer, AddressSerializer
# from companies.serializers import CompanySerializer
from .models import Warehouse
from contacts.serializers import AddressSerializer, ContactSerializer
from .models import WarehouseProduct
from products.serializers import ProductSerializer
from companies.serializers import CompanySerializer
from companies.models import Company

class WarehouseProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = WarehouseProduct
        fields = [ 'product', 'available_quantity', ]
class WarehouseSerializer(serializers.ModelSerializer):
    contact = serializers.StringRelatedField()
    address = serializers.StringRelatedField()
    company = CompanySerializer(read_only=True)
    products = WarehouseProductSerializer(many=True, required=False)
    class Meta:
        model = Warehouse
        fields = ['id', 'warehouse_name', 'products', 'company', 'contact', 'address', 'updated_at', ]
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        company = user.company.id
        # validated_data.pop('products', None)
        print("in warehouse creation")

        company_data = Company.objects.get(pk=company)
        warehouse = Warehouse.objects.create(company=company_data, **validated_data)
        print("Warehouse Added:\n", warehouse)
        return warehouse
