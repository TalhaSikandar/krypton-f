from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView
from django.urls import path
from . import views

urlpatterns = [
    # path('dj-rest-auth/', include('dj_rest_auth.urls')), # new
    # path('api/', include('dj_rest_auth.urls')), # new
    # path('api/registration/', include('dj_rest_auth.registration.urls')), # new
    path('login/', views.LoginView.as_view(), name="user_login"),
    path('logout/', views.LogoutView.as_view(), name="user_logout"),
    path('create/', views.CreateUserView.as_view(), name="user_create "),
    path('delete/', views.DeleteUserView.as_view(), name="user_deletion"),
    path('passwordchange/', views.PasswordChangeView.as_view(), name="password_change"),
    path('passwordchangedone/', views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('', views.index, name="home"),
]
urlpatterns += [
    path('admin_signup/', views.AdminSignupView.as_view(), name='admin_signup'),
]
