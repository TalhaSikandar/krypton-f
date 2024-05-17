from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

from .models import Product
from warehouses.models import Warehouse
from .serializers import ProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                warehouse_pk = self.kwargs.get('warehouse_pk')
                return Product.objects.filter(Warehouse__pk=warehouse_pk)
        # For any other user, return an empty queryset
        return Product.objects.none()
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        warehouse_pk = self.kwargs.get('warehouse_pk')
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                queryset = Product.objects.filter(Warehouse__pk=warehouse_pk, pk=self.kwargs['pk'])
            else:
                # For any other user, return an empty queryset
                queryset = Product.objects.none()

            # Get the specific store object based on URL parameter 'pk'
            obj = get_object_or_404(queryset, pk=self.kwargs['pk'], Warehouse__pk=warehouse_pk)
            return obj
        # If user is not authenticated, return 404 Not Found
        return get_object_or_404(Product.objects.none(), pk=self.kwargs['pk'], Warehouse__pk=warehouse_pk)
