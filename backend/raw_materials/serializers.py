
from rest_framework import serializers
from .models import Rawmaterial


class RawmaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rawmaterial
        fields = ['id', 'rawmaterial_name','unit_weight', 'price', 'description',  'updated_at', ]
