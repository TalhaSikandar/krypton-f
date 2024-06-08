from rest_framework import serializers
from products.serializers import ProductSerializer
from contacts.serializers import ContactSerializer, AddressSerializer
from companies.serializers import CompanySerializer
from .models import Store, StoreProduct
from accounts.serializers import CustomUserSerializer
from accounts.models import CustomUser
from companies.models import Company
from django.contrib.auth.models import Group

class StoreProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = StoreProduct
        fields = ['product','unit_weight', 'available_quantity', ]

class StoreSerializer(serializers.ModelSerializer):
    contact = serializers.StringRelatedField()
    address = serializers.StringRelatedField()
    company = CompanySerializer(read_only=True)
    manager = CustomUserSerializer(read_only=True)
    manager_password = serializers.CharField(write_only=True, required=True)  # New password field
    products = StoreProductSerializer(many=True, required=False)

    class Meta:
        model = Store
        fields = ['id', 'company', 'manager', 'contact', 'products', 'address', 'updated_at', 'manager_password']
        read_only_fields = ['company', 'manager']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        company = user.company.id
        # validated_data.pop('products', None)
        manager_password = validated_data.pop('manager_password')
        print("in store serializer")

        # Create a manager automatically
        company_data = Company.objects.get(pk=company)
        manager_no = CustomUser.objects.filter(company=company_data, role='MANAGER').count() + 1
        manager_email = f"{company_data.company_name.lower()}_manager{manager_no}@{company_data.company_name.lower()}.com"
        manager_username = f"{company_data.company_name.lower()}_manager{manager_no}"
        manager_data = {
            'username': manager_username,
            'email': manager_email,
            'company': company_data,
            'role': 'MANAGER',
            'password': manager_password  # Use the provided password
        }
        print(manager_data) 
        manager = CustomUser.objects.create_user(**manager_data)
        manager_group = Group.objects.get(name='KManager')
        manager.groups.add(manager_group)
        store_data = validated_data.copy()
        products = store_data.pop('products', None)
        store = Store.objects.create(company=company_data ,manager=manager, **store_data)
        if products:
            store.products.set(products)
        manager_email = f"{company_data.company_name.lower()}{store.id}_manager{manager_no}@{company_data.company_name.lower()}.com"
        manager.email = manager_email
        manager.save()
        print("Manager Made") 
        print("Store Added:\n", store)
        return store

    def validate(self, attrs):
        """Custom validation to allow optional products during creation."""
        if not attrs.get('products', None):
            # Allow creation even without products
            return attrs
        else:
            # If products are provided, validate them individually
            for product_data in attrs['products']:
                product_serializer = StoreProductSerializer(data=product_data)
                product_serializer.is_valid(raise_exception=True)  # Raise exception for invalid product data
            return attrs
# class StoreSerializer(serializers.ModelSerializer):
#     contact = serializers.StringRelatedField(read_only=True)
#     address = serializers.StringRelatedField(read_only=True)
#     # company = serializers.StringRelatedField(read_only=True)
#     company = CompanySerializer()
#     manager = CustomUserSerializer()
#     # contact = ContactSerializer(many=True)
#     # address = AddressSerializer(many=True)
#     class Meta:
#         model = Store
#         # fields = ['id', 'store_name', 'company','manager','contact', 'address', 'updated_at', ]
#         fields = ['id', 'company','manager','contact', 'address', 'updated_at', ]
#
#     def create(self, validated_data):
#             request = self.context.get('request')
#             user = request.user
#             company = user.company_code
#
#             # Create a manager automatically
#             manager_no = CustomUser.objects.filter(company_code=company, role='MANAGER').count() + 1
#             manager_email = f"{company.company_name.lower()}_manager{manager_no}@company.com"
#             
#             manager_data = {
#                 'username': f"manager{manager_no}",
#                 'email': manager_email,
#                 'company_code': company,
#                 'role': 'MANAGER',
#                 'password': CustomUser.objects.make_random_password()  # Generate a random password
#             }
#             
#             manager = CustomUser.objects.create(**manager_data)
#             store = Store.objects.create(manager=manager, **validated_data)
#             return store
