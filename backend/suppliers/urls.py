
from django.urls import path
from .views import SupplierDetail, SupplierList

urlpatterns = [
    path('<int:supplier_pk>/', SupplierDetail.as_view(), name="supplier"),
    path('', SupplierList.as_view(), name="suppliers"),
]
