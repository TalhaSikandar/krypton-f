# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
#
# class CustomAuthenticationForm(AuthenticationForm):
#     username = forms.CharField(label='Username')
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#
#     def __init__(self, *args, **kwargs):
#         self.company_code = kwargs.pop('company_code', None)
#         super().__init__(*args, **kwargs)
#         if self.company_code:
#             self.fields['company_code'] = forms.CharField(initial=self.company_code, widget=forms.HiddenInput())
#
#
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser
# import random
# import string
#
# class CustomUserCreationForm(UserCreationForm):
#     company_name = forms.CharField(label='Company Name')
#     address = forms.CharField(label='Address')
#
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields + ('company_name', 'address')
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.address = self.cleaned_data['address']
#         user.company_name = self.cleaned_data['company_name']
#         
#         # Generate company code
#         user.company_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
#
#         if commit:
#             user.save()
#         return user

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'company_code', 'role')  

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'company_code', 'role')  # Customize fields as needed
