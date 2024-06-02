
from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:warehouse_slug>/', views.WarehouseDetail.as_view(), name="warehouse"),
    path('', views.WarehouseList.as_view(), name="warehouses"),
    path('<int:warehouse_pk>/products/', views.WarehouseProductList.as_view(),name="warehouse-products"),
    path('<int:warehouse_pk>/products/<int:product_pk>', views.WarehouseProductList.as_view(),name="warehouse-products"),
]

