from django_filters import rest_framework as filters
from .models import Courses, News


class CoursesFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    created_at = filters.DateFilter(lookup_expr='icontains')
    updated_at = filters.DateFilter(lookup_expr='icontains')
    
    class Meta:
        model = Courses
        fields = ['title', 'created_at', 'updated_at']
        
        
class NewsFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    created_at = filters.DateFilter(lookup_expr='icontains')
    updated_at = filters.DateFilter(lookup_expr='icontains')
    
    class Meta:
        model = News
        fields = ['title', 'created_at', 'updated_at']