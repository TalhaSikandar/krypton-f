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
            print("what", available_quantity)

            # Create or update Rawmaterial object
            rawmaterial, created = Rawmaterial.objects.get_or_create(
                rawmaterial_name=rawmaterial_name,
                unit_weight=unit_weight
            )

            # Create SupplierRawmaterial object
            SupplierRawmaterial.objects.create(supplier=supplier, rawmaterial=rawmaterial, available_quantity=available_quantity)

        return Response(data, status=status.HTTP_201_CREATED)
class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def get_object(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                return get_object_or_404(Supplier.objects.filter(company=user.company), id=self.kwargs['pk'])
        return get_object_or_404(Supplier.objects.none())

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        supplier = serializer.save()
        rawmaterials_data = request.data.get('rawmaterials', [])
        for rawmaterial_data in rawmaterials_data:
            rawmaterial, created = Rawmaterial.objects.get_or_create(
                rawmaterial_name=rawmaterial_data['rawmaterial_name'],
                unit_weight=rawmaterial_data['unit_weight']
            )
            supplier_rawmaterial, created = SupplierRawmaterial.objects.update_or_create(
                supplier=supplier,
                rawmaterial=rawmaterial,
                defaults={
                    'available_quantity': rawmaterial_data.get('available_quantity', 0)
                }
            )
        return Response(serializer.data)



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
        print("here")
        if user.is_authenticated:
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
