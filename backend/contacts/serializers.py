from rest_framework import serializers
from .models import Contact, Address

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'contact_no', 'email', 'website', 'updated_at', ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'city', 'country', 'updated_at', ]
