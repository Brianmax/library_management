from rest_framework import serializers
from .models import CustomUserModel


class CustomUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        read_only_fields = ("__all__")
