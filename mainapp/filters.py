from django_filters import rest_framework as filters
from .models import Courses, News, Lesson, CourseTeacher, Category


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
        
        
class LessonFilter(filters.FilterSet):
    course = filters.CharFilter(lookup_expr='icontains')
    title = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Lesson
        fields = ['course', 'title']
        
        
class CourseTeacherFilter(filters.FilterSet):
    courses = filters.CharFilter(lookup_expr='icontains')
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = CourseTeacher
        fields = ['courses', 'first_name', 'first_name']
        

class CoursesByPriceFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='min_price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='max_price', lookup_expr='lte')
    category = filters.ModelMultipleChoiceFilter(field_name='category', queryset=Category.objects.all())

    class Meta:
        model = Courses
        fields = ['min_price', 'max_price', 'category']
