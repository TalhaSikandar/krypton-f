from rest_framework import serializers
from raw_materials.serializers import RawmaterialSerializer
from .models import Supplier, SupplierRawmaterial
from contacts.models import Contact, Address
from raw_materials.models import Rawmaterial
from contacts.serializers import ContactSerializer, AddressSerializer

class SupplierRawmaterialSerializer(serializers.ModelSerializer):
    rawmaterial = RawmaterialSerializer()

    class Meta:
        model = SupplierRawmaterial
        fields = ['id', 'rawmaterial', 'available_quantity']

class SupplierSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    address = AddressSerializer()
    rawmaterials = SupplierRawmaterialSerializer(many=True, required=False)

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact', 'address', 'industry', 'description', 'rawmaterials']

    def create(self, validated_data):
        print("In creation of supplier here")
        contact_data = validated_data.pop('contact')
        address_data = validated_data.pop('address')
        rawmaterials_data = validated_data.pop('rawmaterials')

        contact, created = Contact.objects.get_or_create(**contact_data)
        address, created = Address.objects.get_or_create(**address_data)

        supplier = Supplier.objects.create(contact=contact, address=address, **validated_data)

        for rawmaterial_data in rawmaterials_data:
            print("Added here", rawmaterial_data)
            rawmaterial_name = rawmaterial_data.get('rawmaterial', {}).get('rawmaterial_name')
            unit_weight = rawmaterial_data.get('rawmaterial', {}).get('unit_weight')
            available_quantity = rawmaterial_data.get('rawmaterial', {}).get('available_quantity')
            print("Name", rawmaterial_name)

            # Create or update Rawmaterial object
            rawmaterial, created = Rawmaterial.objects.get_or_create(
                rawmaterial_name=rawmaterial_name,
                unit_weight=unit_weight
              )
            SupplierRawmaterial.objects.get_or_create(supplier=supplier, rawmaterial=rawmaterial, available_quantity=available_quantity)

        return supplier
