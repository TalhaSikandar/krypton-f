from rest_framework import serializers
from .models import Supplier
from contacts.serializers import ContactSerializer, AddressSerializer

class CompanySerializer(serializers.ModelSerializer):
    # contact = serializers.StringRelatedField(many=True)
    # address = serializers.StringRelatedField(many=True)
    contact = ContactSerializer()
    address = AddressSerializer()
    class Meta:
        model = Company
        fields = ['id', 'name', 'contact', 'address', 'updated_at', ]


