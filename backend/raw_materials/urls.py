from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:rawmaterial_slug>/', views.RawmaterialDetail.as_view(), name="rawmaterial"),
    path('', views.RawmaterialList.as_view(), name="rawmaterials"),
]

