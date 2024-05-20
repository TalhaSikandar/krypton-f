from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response 

from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from django.shortcuts import render
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Store
from contacts.models import Contact, Address
from companies.models import Company
from .serializers import StoreSerializer
from accounts.models import CustomUser
# 1st
#
# # Create your views here.
# @api_view(['GET'])
# def index(request):
#     store = Store.objects.all()
#     storeSerialized = StoreSerializer(store, many=True)
#     return JsonResponse(storeSerialized.data, status=status.HTTP_200_OK, safe=False)
#
# @api_view(['POST'])
# def add_store(request):
#      # Use case: Create a new store
#     store_name = request.data.get('store_name')
#     company_name = request.data.get('company_name',False)
#     company_details = Company.objects.get(company_name=company_name)
#
#     # Contact
#     contact_details_number = request.data.get('contact_number')
#     contact_details_email = request.data.get('contact_email')
#     contact_details_website = request.data.get('contact_website')
#     contact_details = Contact.objects.create(contact_details_number, contact_details_email, contact_details_website)
#
#     # Address
#     address_details_city = request.POST.get('address_city')
#     address_details_country = request.POST.get('address_country')
#     address_details = Address.objects.create(address_details_city, address_details_country)
#
#     new_store = Store.objects.create(store_name, company_details,  contact_details, address_details)
#     new_store.save()
#     return JsonResponse({'message': 'Store was added unsuccessfully!'}, status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['DELETE'])
# def delete_store(request, store_id):
#     store = Store.object.get(pk=store_id)
#     if store:
#         store.delete()
#         return JsonResponse({'message': 'Store was deleted unsuccessfully!'}, status=status.HTTP_204_NO_CONTENT)
#     else:
#         return JsonResponse({'message': 'Store was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
#
#
# 2nd 
# class StoreList(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAdminUser, )
#     # AllowAny - any user, authenticated or not, has full access
#     # IsAuthenticated - only authenticated, registered users have access
#     # IsAdminUser - only admins/superusers have access
#     # IsAuthenticatedOrReadOnly - unauthorized users can view any page, but only
#     # authenticated users have write, edit, or delete privileges
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer
#
# class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer
# 3rd
# class StoreList(generics.ListCreateAPIView):
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer
#
#     def get_permissions(self):
#         if self.request.user.is_authenticated:
#             if self.request.user.groups.filter(name='KAdmin').exists():
#                 return [permissions.IsAuthenticated()]
#             elif self.request.user.groups.filter(name='KManager').exists():
#                 return [permissions.IsAuthenticated(), ManagerStorePermission()]
#         return [permissions.IsAuthenticatedOrReadOnly()]
#
# class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer
#
#     def get_permissions(self):
#         if self.request.user.is_authenticated:
#             if self.request.user.groups.filter(name='KAdmin').exists():
#                 return [permissions.IsAuthenticated(), KAdminCompanyStorePermission()]
#             elif self.request.user.groups.filter(name='KManager').exists():
#                 # KManager can only view and modify its own store
#                 return [permissions.IsAuthenticated(), ManagerStorePermission()]
#         return [permissions.IsAuthenticatedOrReadOnly()]
#
# # Custom permission for KManager to view and modify their own store
# class ManagerStorePermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Check if the user is authenticated
#         if request.user.is_authenticated:
#             # Check if the user is a KManager and if the store belongs to them
#             if request.user.groups.filter(name='KManager').exists():
#                 store_id = view.kwargs.get('pk')  # Assuming the URL parameter is 'pk'
#                 if store_id:
#                     store = Store.objects.filter(pk=store_id, manager=request.user).exists()
#                     return store
#         return False
#
# # Custom permission for KAdmin to view and modify company stores
# class KAdminCompanyStorePermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Check if the user is authenticated and a KAdmin
#         if request.user.is_authenticated and request.user.groups.filter(name='KAdmin').exists():
#             company_id = request.user.company_code_id
#             store_id = view.kwargs.get('pk')  # Assuming the URL parameter is 'pk'
#             if company_id and store_id:
#                 # Check if the store belongs to the KAdmin's company
#                 store = Store.objects.filter(pk=store_id, company_id=company_id).exists()
#                 return store
#         return False

class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print("In Store List")
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                # KAdmins can access stores for their company
                return Store.objects.filter(company=user.company)
            elif user.groups.filter(name='KManager').exists():
                # KManagers can only access their own store
                return Store.objects.filter(manager=user)
        # For any other user, return an empty queryset
        queryset = Store.objects.all() 
        return queryset 
    def create(self, request, *args, **kwargs):
        user = CustomUser.objects.filter(role=CustomUser.Types.ADMIN)[0]
        request.user = user
        print(request.data)
        print(request.user)
        # user = request.user
        if not user.groups.filter(name='KAdmin').exists():
            return Response({'error': 'You are not authorized to create stores.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class StoreDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Store.objects.all() 
    serializer_class = StoreSerializer 
    # permission_classes = [permissions.IsAuthenticated] 
    def get_object(self): 
        user = self.request.user 
        if user.is_authenticated: 
            if user.groups.filter(name='KAdmin').exists(): 
            # KAdmins can access stores for their company 
                queryset = Store.objects.filter(company=user.company) 
            elif user.groups.filter(name='KManager').exists(): 
                 #KManagers can only access their own store 
                queryset = Store.objects.filter(manager=user) 
            else: 
                queryset = Store.objects.none() 
        # If user is not authenticated, 
        return get_object_or_404(queryset, slug=self.kwargs['store_slug'])
