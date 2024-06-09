from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:product_pk>/', views.ProductDetail.as_view(), name="product"),
    path('', views.ProductList.as_view(), name="products"),
    path('<slug:product_slug>/rawmaterial/', include("raw_materials.urls")),
]

