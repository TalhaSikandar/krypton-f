from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

from .models import Rawmaterial
from warehouses.models import Warehouse
from .serializers import RawmaterialSerializer

class RawmaterialList(generics.ListCreateAPIView):
    queryset = Rawmaterial.objects.all()
    serializer_class = RawmaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                warehouse_pk = self.kwargs.get('warehouse_pk')
                return Rawmaterial.objects.filter(Warehouse__pk=warehouse_pk)
        # For any other user, return an empty queryset
        return Rawmaterial.objects.none()
class RawmaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rawmaterial.objects.all()
    serializer_class = RawmaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        warehouse_pk = self.kwargs.get('warehouse_pk')
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                queryset = Rawmaterial.objects.filter(Warehouse__pk=warehouse_pk, pk=self.kwargs['pk'])
            else:
                # For any other user, return an empty queryset
                queryset = Rawmaterial.objects.none()

            # Get the specific store object based on URL parameter 'pk'
            obj = get_object_or_404(queryset, pk=self.kwargs['pk'], Warehouse__pk=warehouse_pk)
            return obj
        # If user is not authenticated, return 404 Not Found
        return get_object_or_404(Rawmaterial.objects.none(), pk=self.kwargs['pk'], Warehouse__pk=warehouse_pk)
