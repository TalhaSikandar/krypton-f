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
from .forms import CustomUserCreationForm  # Import if using a custom form
from .models import CustomUser

def index(request):
    redirect('home.html')
class LoginView(TemplateView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('../home.html')  # Or your desired redirect URL
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        username = request.POST['email']  # Use 'email' field per your model
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('../home.html')  # Or your desired success redirect URL
        else:
            error_message = 'Invalid username or password'
            return self.render_to_response({'error_message': error_message})

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
