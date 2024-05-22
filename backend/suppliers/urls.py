
from django.urls import path
from .views import SupplierDetail, SupplierList

urlpatterns = [
    path('<slug:supplier_slug>/', SupplierDetail.as_view(), name="supplier"),
    path('', SupplierList.as_view(), name="suppliers"),
]
