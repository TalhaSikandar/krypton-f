
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response 

from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from django.shortcuts import render
from rest_framework import status
from django.shortcuts import get_object_or_404
from suppliers.models import SupplierRawmaterial

from raw_materials.serializers import RawmaterialSerializer
from suppliers.serializers import SupplierRawmaterialSerializer

from .models import Warehouse, WarehouseProduct
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
        return get_object_or_404(queryset, pk=self.kwargs['warehouse_pk'])

from .serializers import WarehouseProductSerializer
from products.models import Product, ProductRawmaterial
from raw_materials.models import Rawmaterial
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view, permission_classes

class WarehouseProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = WarehouseProductSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.groups.filter(name='KAdmin').exists():
            warehouse = Warehouse.objects.get(id=self.kwargs.get('warehouse_pk'))
            return WarehouseProduct.objects.filter(warehouse=warehouse)
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
        available_quantity = product_data['available_quantity']
        description = product_data.get('description', '')
        # warehouses = Product.warehoues.all()
        # print(warehouses)

        product, created = Product.objects.update_or_create(
            product_name=product_name,
            defaults={
                'unit_weight': unit_weight,
                'description': description
            }
        )

        WarehouseProduct.objects.update_or_create(warehouse=warehouse, product=product, available_quantity=available_quantity)

        # Add the product to the warehouse
        warehouse.products.add(product)

        raw_materials_data = product_data.get('raw_materials', [])
        for material_data in raw_materials_data:
            rawmaterial = material_data['rawmaterial']
            required_quantity = material_data['required_quantity']
            print(rawmaterial['id'], "yeah")

            raw_material = Rawmaterial.objects.get(id=rawmaterial['id'])

            ProductRawmaterial.objects.update_or_create(
                product=product,
                raw_material=raw_material,
                required_quantity=required_quantity
            )

        serializer = ProductSerializer(product, context={'request': request})
        print(serializer.data, "yes data")
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
from suppliers.models import Supplier
class RawmaterialList(generics.ListCreateAPIView):
    queryset = SupplierRawmaterial.objects.all()
    serializer_class = SupplierRawmaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                suppliers_rawmaterials = SupplierRawmaterial.objects.filter(supplier__company=user.company)
                # suppliers = []
                # for supplier_r in suppliers_rawmaterials:
                #     suppliers.append(Supplier.objects.get(id=supplier_r.supplier.id))
                #
                # for j in range(len(suppliers_rawmaterials)):
                #     suppliers_rawmaterials[j].supplier.id = suppliers[j]
                print(suppliers_rawmaterials, "all`")
                return suppliers_rawmaterials
        # For any other user, return an empty queryset
        print("inasdfasdf rawmaterial list")
        return get_object_or_404(SupplierRawmaterial.objects.none())

class ProductList(generics.ListCreateAPIView):
    queryset = WarehouseProduct.objects.all()
    serializer_class = WarehouseProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                warehouse_products = WarehouseProduct.objects.filter(warehouse__company=user.company)
                # suppliers = []
                # for supplier_r in suppliers_rawmaterials:
                #     suppliers.append(Supplier.objects.get(id=supplier_r.supplier.id))
                #
                # for j in range(len(suppliers_rawmaterials)):
                #     suppliers_rawmaterials[j].supplier.id = suppliers[j]
                print(warehouse_products, "all`")
                return warehouse_products
        # For any other user, return an empty queryset
        print("inasdfasdf product list")
        return get_object_or_404(WarehouseProduct.objects.none())
