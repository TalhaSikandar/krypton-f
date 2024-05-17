
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.StoreDetail.as_view(), name="store"),
    path('', views.StoreList.as_view(), name="stores"),
]

