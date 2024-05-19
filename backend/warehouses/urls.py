
from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:warehouse_slug>/', views.WarehouseDetail.as_view(), name="warehouse"),
    path('', views.WarehouseList.as_view(), name="warehouses"),
    path('<slug:warehouse_slug>/products/', include("products.urls")),
]

