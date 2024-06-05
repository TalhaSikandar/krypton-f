
from django.urls import path
from .views import SupplierDetail, SupplierList, SupplierRawmaterialDetail, SupplierRawmaterialList

urlpatterns = [
    path('<int:supplier_pk>/', SupplierDetail.as_view(), name="supplier"),
    path('<int:supplier_pk>/raw_materials/', SupplierRawmaterialList.as_view(), name="supplier_rawmaterials"),
    path('<int:supplier_pk>/raw_materials/<int:raw_material_pk>/', SupplierRawmaterialDetail.as_view(), name="supplier_rawmaterial"),
    path('', SupplierList.as_view(), name="suppliers"),
]
