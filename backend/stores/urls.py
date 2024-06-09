
from django.urls import path
from . import views
from products.views import ProductDetail

urlpatterns = [
    path('products/', views.StoresProductList.as_view(),name="stores-products"),
    path('<int:store_pk>/', views.StoreDetail.as_view(), name="store"),
    path('', views.StoreList.as_view(), name="stores"),
    path('<slug:store_slug>/add-product/', views.add_product_to_store, name='add-product-to-store'),
    path('<int:store_pk>/products/', views.StoreProductList.as_view(),name="store-products"),
    path('<int:product_pk>/products_r/', ProductDetail.as_view(),name="special"),
    path('<int:store_pk>/products/<int:product_pk>/', views.StoreProductDetail.as_view(),name="store-products"),
]

