from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id',
        read_only=True, format='hex')
    date_joined = serializers.DateTimeField(read_only=True)
    
    
    class Meta:
        model = CustomUser
        fields =  ['id', 'username', 'first_name',
        'last_name', 'avatar', 'email', 'age',
        'is_active', 'date_joined']
        read_only_field = ['is_active']