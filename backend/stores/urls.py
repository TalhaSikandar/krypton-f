
from django.urls import path
from . import views

urlpatterns = [
    path('<slug:store_slug>/', views.StoreDetail.as_view(), name="store"),
    path('', views.StoreList.as_view(), name="stores"),
    path('<slug:store_slug>/add-product/', views.add_product_to_store, name='add-product-to-store'),
]

