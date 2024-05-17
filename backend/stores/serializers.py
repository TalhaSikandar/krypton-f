from rest_framework import serializers
from contacts.serializers import ContactSerializer, AddressSerializer
from companies.serializers import CompanySerializer
from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    contact = serializers.StringRelatedField(read_only=True)
    address = serializers.StringRelatedField(read_only=True)
    company = serializers.StringRelatedField(read_only=True)
    # contact = ContactSerializer(many=True)
    # address = AddressSerializer(many=True)
    class Meta:
        model = Store
        # fields = ['id', 'store_name', 'company','manager','contact', 'address', 'updated_at', ]
        fields = ['id', 'company','manager','contact', 'address', 'updated_at', ]
