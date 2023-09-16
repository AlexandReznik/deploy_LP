from rest_framework.serializers import HyperlinkedModelSerializer
from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id',
        read_only=True, format='hex')
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = CustomUser
        fields =  ['id', 'username', 'first_name',
        'last_name', 'avatar', 'email', 'date_of_birth',
        'is_active', 'created_at', 'updated_at']
        read_only_field = ['is_active']