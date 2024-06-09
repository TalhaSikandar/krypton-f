from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

from .models import Product
from rest_framework.response import Response
from warehouses.models import Warehouse
from .serializers import ProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            pr = Product.objects.filter(id=self.kwargs.get('product_pk'))
            return pr

        return Product.objects.all()

class ProductDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    # permission_classes = [permissions.IsAuthenticated] 
    def get_object(self): 
        user = self.request.user 
        if self.request.user.is_authenticated:
            pr = Product.objects.get(id=self.kwargs.get('product_pk'))
            return pr
        # If user is not authenticated, 
        return Response(status=status.HTTP_204_NO_CONTENT)
