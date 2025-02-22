# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import AuthenticationForm
# from .forms import CustomAuthenticationForm, CustomUserCreationForm
# from .models import CustomUser
#
# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Store company code in session after first signup
#             request.session['company_code'] = user.company_code
#             return redirect('signin.html')  # Redirect to login after signup
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'signup.html', {'form': form})
#
# def signin(request):
#     company_code = request.session.get('company_code')
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(data=request.POST, company_code=company_code)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             
#             # Retrieve user based on username, company code, and password
#             user = authenticate(username=username, password=password)
#             if user is not None and user.company_code == company_code:
#                 login(request, user)
#                 return redirect('dashboard.html')  # Redirect to dashboard after successful login
#             else:
#                 form.add_error(None, 'Invalid company code or credentials')
#     else:
#         form = CustomAuthenticationForm(company_code=company_code)
#     return render(request, 'signin.html', {'form': form})
#
# def logout(request):
#     logout(request)
#     redirect('login.html')
#
# def index(request):
#     redirect('index.html')
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, View, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from rest_framework import generics, permissions

from .serializers import CustomUserSerializer
from .forms import CustomUserCreationForm  # Import if using a custom form
from .models import CustomUser

def index(request):
    redirect('home.html')
class EmployeeList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='KAdmin').exists():
                users = CustomUser.objects.filter(company=user.company)
                print(users, "Hi")
                # KAdmins can access Warehouse for their company
                return CustomUser.objects.filter(company=user.company)
        # For any other user, return an empty queryset
        queryset = CustomUser.objects.none()
        return queryset 


class LoginView(TemplateView):
    template_name = 'login.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('../home.html')  # Or your desired redirect URL
    #     return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
            content_type = request.content_type
            if content_type == 'application/x-www-form-urlencoded':
                email = request.POST.get('email')
                password = request.POST.get('password')
            elif content_type == 'application/json':
                try:
                    data = json.loads(request.body)
                    email = data.get('email')
                    password = data.get('password')
                except json.JSONDecodeError:
                    return JsonResponse({'error': 'Invalid JSON data'}, status=400)
            else:
                return JsonResponse({'error': 'Unsupported content type'}, status=400)

            if email and password:
                user = authenticate(request, username=email, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                    return JsonResponse({'message': 'Login successful'})
                else:
                    return JsonResponse({'error': 'Invalid username or password'}, status=400)
            else:
                return JsonResponse({'error': 'Email and password are required'}, status=400)
class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')  # Or your desired logout redirect URL


# Editing Accounts
from django.contrib.auth.models import Group
def index(request):
    render(request, template_name='home.html')
class CreateUserView(CreateView):
    print("User Being Created")
    model = CustomUser
    form_class = CustomUserCreationForm  # Use custom form if defined
    success_url = '../home.html'  # Or your desired redirect URL for successful creation
    template_name = 'create_user.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('../home.html')  # Or your desired redirect URL
    #     return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
            self.object = form.save()  # Save the created user
            user = self.object  # Now you can access the created user instance
            # Check role and add to group
            if user.role == CustomUser.Types.ADMIN:  # Replace with your role logic
                admin_group = Group.objects.get(name='KAdmin')
                user.groups.add(admin_group)
                print("Yes, an Admin added to the group")
            elif user.role == CustomUser.Types.MANAGER:  # Add logic for other roles
                manager_group = Group.objects.get(name='KManager')
                user.groups.add(manager_group)
                print("Yes, a manager added to the group")
            self.object = form.save()  # Save the created user
            return super().form_valid(form)

class UserDetail(generics.RetrieveAPIView): 
    queryset = CustomUser.objects.all() 
    serializer_class = CustomUserSerializer 
    # permission_classes = [permissions.IsAuthenticated] 
    def get_object(self): 
        user = self.request.user 
        if user.is_authenticated: 
            if user.groups.filter(name='KAdmin').exists(): 
            # KAdmins can access stores for their company 
                return CustomUser.objects.get(id=user.id) 
        # If user is not authenticated, 
        return CustomUser.objects.none() 
        
class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    success_url = 'login'  # Or your desired redirect URL for successful deletion
    template_name = 'delete_user.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_object(self, queryset=None):
            user_to_delete = super().get_object(queryset=queryset)
            if not self.request.user.groups.filter(name='KAdmin').exists():
                raise PermissionError('You are not authorized to delete users.')
            return user_to_delete
class UserPasswordChangeView(PasswordChangeView):
    model = CustomUser
    success_url = 'home.html'  # Or your desired redirect URL after successful password change
    template_name = 'password_change_form.html'

class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'password_change_done.html'

from django.contrib.auth.forms import PasswordChangeForm
from rest_framework import permissions
class CustomPasswordChangeView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.data)
        if form.is_valid():
            user = form.save()
            return JsonResponse({'message': 'Password changed successfully'})
        else:
            errors = form.errors.get_json_data()
            print(errors, "ok")
            return JsonResponse({'errors': errors}, status=400)
from django.shortcuts import get_object_or_404
from stores.models import Store
class CustomDeleteUserView(generics.GenericAPIView):
    model = CustomUser
    permission_classes = [permissions.IsAuthenticated]


    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        if not request.user.groups.filter(name='KAdmin').exists():
            raise PermissionError('You are not authorized to delete users.')

        user = get_object_or_404(CustomUser, pk=user_id)
        store = Store.objects.get(manager=user)
        store.manager=self.request.user
        store.save()
        user.delete()

        return JsonResponse({'message': 'User deleted successfully'})

    def get_success_url(self):
        # This is not used, but required by DeleteView
        return reverse_lazy('employees')  # Redirect to a view after deletion
from django.urls import reverse_lazy
from companies.models import Company
from rest_framework import status
from django.http import JsonResponse
import json
class AdminSignupView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user_login')

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)

        company_id = data.get('company_id')
        print(company_id)
        if not company_id:
            return JsonResponse({'error': 'Company ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return JsonResponse({'error': 'Invalid company ID'}, status=status.HTTP_400_BAD_REQUEST)

        # Add company and role to the data
        data['company'] = company.id
        data['role'] = CustomUser.Types.ADMIN  # Assuming CustomUser model
        form = self.form_class(data)
        print(form.is_valid())
        if form.is_valid():
            user = form.save(commit=False)
            user.company = company
            user.role = CustomUser.Types.ADMIN
            user.save()
            admin_group = Group.objects.get(name='KAdmin')
            user.groups.add(admin_group)
            # Clear the session data after use (optional, not strictly necessary)
            print("User Created")
            return JsonResponse({'username': user.email}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(form.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow unauthenticated requests
def custom_token_obtain_view(request):
    # Your authentication logic to validate credentials and issue tokens
    # Example logic: (Replace with your actual authentication logic)
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        # Validate credentials (Example: using Django User model)
        user = authenticate(username=username, password=password)
        if user:
            # Issue tokens using SimpleJWT
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            print(user.company.id, "com")
            return Response({'access_token': access_token, 'refresh': refresh_token, 'username' : user.username, 'company_name' : user.company.company_name, 'company_id': user.company.id}, status=status.HTTP_200_OK)
    
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def custom_token_refresh_view(request):
    refresh_token = request.data.get('refresh')
    if refresh_token:
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            return Response({'access': access_token}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'error': 'Refresh token not provided'}, status=status.HTTP_400_BAD_REQUEST)
