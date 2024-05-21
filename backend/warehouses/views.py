
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
