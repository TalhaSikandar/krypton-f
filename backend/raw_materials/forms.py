from django.forms import ModelForm
from .models import Rawmaterial


class RawmaterialForm(ModelForm):
    class Meta:
        model = Rawmaterial
        fields = "__all__"
        # exclude = ['store_name']
