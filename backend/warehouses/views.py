
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
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                # KAdmins can access stores for their company
                return Warehouse.objects.filter(company=user.company_code)
        # For any other user, return an empty queryset
        return Warehouse.objects.none()
class WarehouseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                # KAdmins can access stores for their company
                queryset = Warehouse.objects.filter(company=user.company_code)
            else:
                # For any other user, return an empty queryset
                queryset = Warehouse.objects.none()

            # Get the specific store object based on URL parameter 'pk'
            obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
            return obj
        # If user is not authenticated, return 404 Not Found
        return get_object_or_404(Warehouse.objects.none(), pk=self.kwargs['pk'])
