from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetail.as_view(), name="product"),
    path('', views.ProductList.as_view(), name="products"),
    path('<int:product_pk>/rawmaterial/', include("raw_materials.urls")),
]

