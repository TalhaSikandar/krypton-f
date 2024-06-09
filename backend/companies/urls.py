from django.urls import path
from .views import CompanySignupView, get_csrf_token


# accounts/urls.py

from django.urls import path
from .views import CompanyList, CompanyDetail
from accounts.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', CompanySignupView.as_view(), name='company_signup'),
    path('csrf/', get_csrf_token, name='csrf_token'),
]

urlpatterns += [
    path('<int:pk>/', CompanyDetail.as_view(), name="company"),
    path('', CompanyList.as_view(), name="companies"),
]

