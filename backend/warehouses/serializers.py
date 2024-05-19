
from rest_framework import serializers
# from contacts.serializers import ContactSerializer, AddressSerializer
# from companies.serializers import CompanySerializer
from .models import Warehouse
from contacts.serializers import AddressSerializer, ContactSerializer


class WarehouseSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    contact = ContactSerializer()
    # contact = serializers.StringRelatedField()
    # address = serializers.StringRelatedField()
    company = serializers.StringRelatedField(read_only=True)
    products = serializers.StringRelatedField(read_only=True)
    # contact = ContactSerializer(many=True)
    # address = AddressSerializer(many=True)
    class Meta:
        model = Warehouse
        fields = ['id', 'warehouse_name', 'products', 'company', 'contact', 'address', 'updated_at', ]
