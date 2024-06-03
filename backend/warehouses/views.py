
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response 

from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from django.shortcuts import render
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Warehouse
from contacts.models import Contact, Address
from companies.models import Company
from .serializers import WarehouseSerializer

class WarehouseList(generics.ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                # KAdmins can access Warehouse for their company
                return Warehouse.objects.filter(company=user.company)
        # For any other user, return an empty queryset
        queryset = Warehouse.objects.none()
        return queryset 
    def create(self, request, *args, **kwargs):
        user = self.request.user
        if not user.groups.filter(name='KAdmin').exists():
            return Response({'error': 'You are not authorized to create Warehouses.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(data=request.data, context={'request': request})
        print("In Warehouse Creation")
        if not serializer.is_valid():
                    print(serializer.errors)  # Print the serializer errors for debugging
                    return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class WarehouseDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Warehouse.objects.all() 
    serializer_class = WarehouseSerializer 
    # permission_classes = [permissions.IsAuthenticated] 
    def get_object(self): 
        user = self.request.user 
        if user.is_authenticated: 
            if user.groups.filter(name='KAdmin').exists(): 
            # KAdmins can access stores for their company 
                queryset = Warehouse.objects.filter(company=user.company) 
            else: 
                queryset = Warehouse.objects.none() 
        # If user is not authenticated, 
        return get_object_or_404(queryset, slug=self.kwargs['warehouse_slug'])

from .serializers import WarehouseProductSerializer
from products.models import Product, ProductRawmaterial
from raw_materials.models import Rawmaterial
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view, permission_classes

class WarehouseProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.groups.filter(name='KAdmin').exists():
            warehouse_pk = self.kwargs.get('warehouse_pk')
            return Product.objects.filter(warehouses__id=warehouse_pk)
        return Product.objects.none()

    def create(self, request, *args, **kwargs):
        user = self.request.user
        warehouse_pk = self.kwargs.get('warehouse_pk')
        warehouse = get_object_or_404(Warehouse, pk=warehouse_pk)

        if not user.groups.filter(name='KAdmin').exists() or user.company != warehouse.company:
            return Response({'error': 'You are not authorized to create products for this warehouse.'}, status=status.HTTP_403_FORBIDDEN)

        product_data = request.data
        product_name = product_data['product_name']
        unit_weight = product_data['unit_weight']
        description = product_data.get('description', '')

        product, created = Product.objects.get_or_create(
            product_name=product_name,
            defaults={
                'unit_weight': unit_weight,
                'description': description
            }
        )

        # Add the product to the warehouse
        warehouse.products.add(product)

        raw_materials_data = product_data.get('raw_materials', [])
        for material_data in raw_materials_data:
            rawmaterial_name = material_data['name']
            quantity = material_data['quantity']
            material_unit_weight = material_data['unit_weight']

            raw_material, created = Rawmaterial.objects.get_or_create(
                rawmaterial_name=rawmaterial_name,
                defaults={'unit_weight': material_unit_weight}
            )

            ProductRawmaterial.objects.create(
                product=product,
                raw_material=raw_material,
                required_quantity=quantity
            )

        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class WarehouseProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        warehouse_pk = self.kwargs.get('warehouse_pk')
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                queryset = Product.objects.filter(Warehouses__pk=warehouse_pk, pk=self.kwargs['product_pk'])
            else:
                # For any other user, return an empty queryset
                queryset = Product.objects.none()

            # Get the specific store object based on URL parameter 'pk'
            obj = get_object_or_404(queryset, pk=self.kwargs['product_pk'], warehouses__pk=warehouse_pk)
            return obj
        # If user is not authenticated, return 404 Not Found
        return get_object_or_404(Product.objects.none(), pk=self.kwargs['product_pk'], warehouses__pk=warehouse_pk)
