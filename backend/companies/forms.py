
# companies/forms.py

from django import forms
from .models import Company

class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'contact', 'address', 'website', 'industry', 'description', ]
