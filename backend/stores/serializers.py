from rest_framework import serializers
from products.serializers import ProductSerializer
from contacts.serializers import ContactSerializer, AddressSerializer
from companies.serializers import CompanySerializer
from .models import Store, StoreProduct
from accounts.serializers import CustomUserSerializer
from accounts.models import CustomUser
from companies.models import Company

class StoreProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = StoreProduct
        fields = ['product', 'quantity']

class StoreSerializer(serializers.ModelSerializer):
    contact = serializers.StringRelatedField()
    address = serializers.StringRelatedField()
    company = CompanySerializer(read_only=True)
    manager = CustomUserSerializer(read_only=True)
    manager_password = serializers.CharField(write_only=True, required=True)  # New password field
    products = StoreProductSerializer(source='storeproduct_set', many=True)

    class Meta:
        model = Store
        fields = ['id', 'company', 'manager', 'contact', 'products', 'address', 'updated_at', 'manager_password']
        read_only_fields = ['company', 'manager']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        company = user.id

        manager_password = validated_data.pop('manager_password')

        # Create a manager automatically
        company_data = Company.objects.get(pk=company)
        manager_no = CustomUser.objects.filter(company=company, role='MANAGER').count() + 1
        manager_email = f"{company_data.company_name.lower()}_manager{manager_no}@company.com"
        
        manager_data = {
            'username': f"manager{manager_no}",
            'email': manager_email,
            'company': company_data,
            'role': 'MANAGER',
            'password': manager_password  # Use the provided password
        }
        
        manager = CustomUser.objects.create_user(**manager_data)
        store = Store.objects.create(company=company_data ,manager=manager, **validated_data)
        print("Store Added:\n", store)
        return store
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
