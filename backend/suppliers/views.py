from rest_framework import generics
from .serializers import SupplierSerializer
from .models import Supplier, SupplierRawmaterial
class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                # KAdmins can access stores for their company
                return Supplier.objects.filter(company=user.company)
        # For any other user, return an empty queryset
        queryset = Company.objects.all() 
        return queryset 
    def create(self, request, *args, **kwargs):
        user = request.user
        print(request.data)
        print(request.user)
        if not user.groups.filter(name='KAdmin').exists():
            return Response({'error': 'You are not authorized to create Suppliers.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class SupplierDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Supplier.objects.all() 
    serializer_class = SupplierRawmaterial 
    # permission_classes = [permissions.IsAuthenticated] 
    def get_object(self): 
        user = self.request.user 
        if user.is_authenticated: 
            if user.groups.filter(name='KAdmin').exists(): 
            # KAdmins can access stores for their company 
                queryset = Supplier.objects.filter(company=user.company) 
            else: 
                queryset = Company.objects.none() 
        # If user is not authenticated, 
        return get_object_or_404(queryset, slug=self.kwargs['company_slug'])
