from rest_framework import generics, status
from contacts.models import Contact, Address
from contacts.serializers import ContactSerializer, AddressSerializer
from .serializers import SupplierSerializer
from .models import Supplier, SupplierRawmaterial
from raw_materials.models import Rawmaterial
from rest_framework.response import Response 


class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.role == 'ADMIN':
            # print("here valid", Supplier.objects.filter(company=user.company))
            return Supplier.objects.filter(company=user.company)
        return Supplier.objects.none()

    def create(self, request, *args, **kwargs):
        user = request.user

        if user.role != 'ADMIN':
            return Response({'error': 'You are not authorized to create Suppliers.'}, status=status.HTTP_403_FORBIDDEN)

        # Extract data from request
        data = request.data

        # Contact details
        contact_data = data.get('contact', {})
        contact, created = Contact.objects.get_or_create(**contact_data)

        # Address details
        address_data = data.get('address', {})
        address, created = Address.objects.get_or_create(**address_data)

        # Supplier details (excluding contact and address)
        supplier_data = {field: value for field, value in data.items() if field not in ('contact', 'address', 'rawmaterials')}

        # Create supplier object
        supplier = Supplier.objects.create(company=user.company, contact=contact, address=address, **supplier_data)

        # Handle raw materials
        rawmaterials_data = data.get('rawmaterials', [])
        for rawmaterial_data in rawmaterials_data:
            # Extract raw material details
            print("check", rawmaterial_data)
            rawmaterial_name = rawmaterial_data.get('rawmaterial', {}).get('rawmaterial_name')
            unit_weight = rawmaterial_data.get('rawmaterial', {}).get('unit_weight')
            available_quantity = rawmaterial_data.get('rawmaterial',{}).get('available_quantity')
            price = rawmaterial_data.get('rawmaterial', {}).get('price_per_unit')
            print("what", available_quantity)

            # Create or update Rawmaterial object
            rawmaterial, created = Rawmaterial.objects.get_or_create(
                rawmaterial_name=rawmaterial_name,
                unit_weight=unit_weight,
                price=price
            )

            # Create SupplierRawmaterial object
            SupplierRawmaterial.objects.create(supplier=supplier, rawmaterial=rawmaterial, available_quantity=available_quantity)

        return Response(data, status=status.HTTP_201_CREATED)
class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer  # Use serializer for update functionality

    def get_object(self):
        user = self.request.user
        if user.is_authenticated and user.groups.filter(name='KAdmin').exists():
            return get_object_or_404(Supplier, pk=self.kwargs['supplier_pk'])
        return get_object_or_404(Supplier.objects.none())

    def retrieve(self, request, *args, **kwargs):
        print("im in retreive")
        instance = self.get_object()
        supplier_data = self.construct_supplier_data(instance)
        print(supplier_data, "supplier_data")
        return Response(supplier_data)

    def construct_supplier_data(self, instance):
        supplier_data = {
            'id': instance.id,
            'name': instance.name,
            'contact': {
                'contact_no': instance.contact.contact_no if instance.contact else '',
                'email': instance.contact.email if instance.contact else '',
            },
            'address': {
                'city': instance.address.city if instance.address else '',
                'country': instance.address.country if instance.address else '',
            },
            'industry': instance.industry,
            'description': instance.description,
            'rawmaterials': []
        }

        supplier_rawmaterials = SupplierRawmaterial.objects.filter(supplier=instance)
        print(supplier_rawmaterials, "complete data")
        for supraw in supplier_rawmaterials:
            rawmaterial = supraw.rawmaterial
            supplier_data['rawmaterials'].append({
                'rawmaterial_name': rawmaterial.rawmaterial_name,
                'available_quantity': supraw.available_quantity,
                'unit_weight': rawmaterial.unit_weight,
                'price_per_unit': rawmaterial.price,
                'rawmaterial_id': rawmaterial.id,
                'is_deleted': False
            })

        return supplier_data

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        supplier_data = {
            'name': request.data.get('name', instance.name),
            'contact': request.data.get('contact', {}),
            'address': request.data.get('address', {}),
            'industry': request.data.get('industry', instance.industry),
            'description': request.data.get('description', instance.description),
            'rawmaterials': request.data.get('rawmaterials', [])
        }

        instance.name = supplier_data['name']
        instance.industry = supplier_data['industry']
        instance.description = supplier_data['description']
        
        if supplier_data['contact']:
            instance.contact.contact_no = supplier_data['contact'].get('contact_no', instance.contact.contact_no)
            instance.contact.email = supplier_data['contact'].get('email', instance.contact.email)
            instance.contact.save()

        if supplier_data['address']:
            instance.address.city = supplier_data['address'].get('city', instance.address.city)
            instance.address.country = supplier_data['address'].get('country', instance.address.country)
            instance.address.save()

        instance.save()
        print("length", supplier_data['rawmaterials'])
        count = 0
        for rawmaterial_data in supplier_data['rawmaterials']:
            if rawmaterial_data['is_deleted']:
                Rawmaterial.objects.get(id=rawmaterial_data['rawmaterial_id']).delete()
                continue
            rawmaterial, created = Rawmaterial.objects.get_or_create(
                rawmaterial_name=rawmaterial_data['rawmaterial_name'],
                unit_weight=rawmaterial_data['unit_weight'],
                price=rawmaterial_data['price_per_unit']
            )
            SupplierRawmaterial.objects.update_or_create(
                supplier=instance,
                rawmaterial=rawmaterial,
                defaults={
                    'available_quantity': rawmaterial_data.get('available_quantity', 0)
                }
            )
            count = count + 1

        print("count", count)
        return Response(self.construct_supplier_data(instance))



from raw_materials.serializers import RawmaterialSerializer
from .serializers import SupplierRawmaterialSerializer
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

class SupplierRawmaterialList(generics.ListCreateAPIView):
    queryset = SupplierRawmaterial.objects.all()
    serializer_class = SupplierRawmaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            print("in rawmaterial list")
            if user.groups.filter(name='KAdmin').exists():
                supplier_pk = self.kwargs.get('supplier_pk')
                supplier = Supplier.objects.get(pk=supplier_pk)
                print(supplier,"supplier")
                if supplier.company == user.company:
                    # testObj=SupplierRawmaterial.objects.filter(supplier=supplier).first()
                    # print("yes")
                    # print(testObj.available_quantity)
                    return SupplierRawmaterial.objects.filter(supplier=supplier)
        # For any other user, return an empty queryset
        return get_object_or_404(SupplierRawmaterial.objects.none())
class SupplierRawmaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rawmaterial.objects.all()
    serializer_class = RawmaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        print("in rawmaterial detail")
        user = self.request.user
        supplier_pk = self.kwargs.get('supplier_pk')
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                queryset = Rawmaterial.objects.filter(suppliers__pk=supplier_pk, pk=self.kwargs['raw_material_pk'])
            else:
                # For any other user, return an empty queryset
                queryset = Rawmaterial.objects.none()

            # Get the specific store object based on URL parameter 'pk'
            obj = get_object_or_404(queryset, pk=self.kwargs['raw_material_pk'], suppliers__pk=supplier_pk)
            return obj
        # If user is not authenticated, return 404 Not Found
        return get_object_or_404(Rawmaterial.objects.none(), pk=self.kwargs['raw_material_pk'], suppliers__pk=supplier_pk)
