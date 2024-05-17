
from django.forms import ModelForm
from .models import Warehouse


class WarehouseForm(ModelForm):
    class Meta:
        model = Warehouse
        fields = "__all__"
        # exclude = ['store_name']
