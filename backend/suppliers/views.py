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
            return Supplier.objects.filter(company=user.company)
        return Supplier.objects.none()

    def create(self, request, *args, **kwargs):
        user = request.user

        if user.role != 'ADMIN':
            return Response({'error': 'You are not authorized to create Suppliers.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(data=request.data, context={'request': request})
        print("RequestData", request.data)
        if not serializer.is_valid():
            print(serializer.errors)  # Print the serializer errors for debugging
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        # serializer.save()
        # print("not going to serializer")
        # serializer.is_valid(raise_exception=True)
        supplier = serializer.save(company=user.company)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
