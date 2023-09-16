from django_filters import rest_framework as filters
from .models import CustomUser


class CustomUserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr='icontains')
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    date_of_birth = filters.DateFilter(lookup_expr='icontains')
    
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'date_of_birth']