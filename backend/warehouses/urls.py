
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.WarehouseDetail.as_view(), name="warehouse"),
    path('', views.WarehouseList.as_view(), name="warehouses"),
    path('<int:warehouse_pk>/products/', include("products.urls")),
]

