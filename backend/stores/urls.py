
from django.urls import path
from . import views

urlpatterns = [
    path('<slug:store_slug>/', views.StoreDetail.as_view(), name="store"),
    path('', views.StoreList.as_view(), name="stores"),
]

