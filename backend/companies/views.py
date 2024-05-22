from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Company
from .forms import CompanyRegistrationForm
from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser
from django.http import JsonResponse
from django.middleware.csrf import get_token

# class CompanySignupView(CreateView):
#     model = Company
#     form_class = CompanyRegistrationForm
#     success_url = reverse_lazy('admin_signup')
#
#     def form_valid(self, form):
#         self.object = form.save()
#         print(self.object)
#         self.request.session['company_id'] = self.object.id
#         response = {
#             'company_id': self.object.id,
#             'success_url': self.get_success_url()
#         }
#         print("In Sign Up: Response")
#         print(response)
#         return JsonResponse(response, status=HTTP_201_CREATED)
#
#     def form_invalid(self, form):
#         print("Form is invalid")
#         print(form.errors)
#         return JsonResponse(form.errors, status=400)
#
#     def post(self, request, *args, **kwargs):
#         print("POST request received")
#         print(request.POST)
#         print(request)
#         return super().post(request, *args, **kwargs)
#
import json
from contacts.models import Contact
from contacts.models import Address

class CompanySignupView(CreateView):
    model = Company
    form_class = CompanyRegistrationForm
    success_url = reverse_lazy('admin_signup')

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        company_data = {
            'company_name': data['company_name']
        }

        # Create or get Contact
        contact_detail = data['contact']
        if contact_detail:
            contact, created = Contact.objects.get_or_create(contact_detail)
            company_data['contact'] = contact.id
        else:
            return JsonResponse({'contact': ['This field is required.']}, status=400)

        # Create or get Address
        address_detail = data['address']
        if address_detail:
            address, created = Address.objects.get_or_create(address_detail)
            company_data['address'] = address.id
        else:
            return JsonResponse({'address': ['This field is required.']}, status=400)

        form = self.form_class(company_data)
        if form.is_valid():
            self.object = form.save()
            self.request.session['company_id'] = self.object.id
            response = {
                'company_id': self.object.id,
                'success_url': self.get_success_url()
            }
            print(self.request)
            return JsonResponse(response, status=201)
        else:
            return JsonResponse(form.errors, status=400)

# For CSRF token
def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})


from rest_framework import generics
from .serializers import CompanySerializer
class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                # KAdmins can access stores for their company
                return Company.objects.filter(company=user.company)
            elif user.groups.filter(name='KManager').exists():
                # KManagers can only access their own store
                return Company.objects.filter(manager=user)
        # For any other user, return an empty queryset
        queryset = Company.objects.all() 
        return queryset 
    def create(self, request, *args, **kwargs):
        user = request.user
        print(request.data)
        print(request.user)
        if not user.groups.filter(name='KAdmin').exists():
            return Response({'error': 'You are not authorized to create companies.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Company.objects.all() 
    serializer_class = CompanySerializer 
    # permission_classes = [permissions.IsAuthenticated] 
    def get_object(self): 
        user = self.request.user 
        if user.is_authenticated: 
            if user.groups.filter(name='KAdmin').exists(): 
            # KAdmins can access stores for their company 
                queryset = Company.objects.filter(company=user.company) 
            elif user.groups.filter(name='KManager').exists(): 
                 #KManagers can only access their own store 
                queryset = Company.objects.filter(manager=user) 
            else: 
                queryset = Company.objects.none() 
        # If user is not authenticated, 
        return get_object_or_404(queryset, slug=self.kwargs['company_slug'])
