from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

from .models import Product
from warehouses.models import Warehouse
from .serializers import ProductSerializer

