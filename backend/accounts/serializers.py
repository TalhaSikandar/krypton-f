
from rest_framework import serializers
from accounts.models import CustomUser  # Import your CustomUser model

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'company', 'profile_picture', 'role']
