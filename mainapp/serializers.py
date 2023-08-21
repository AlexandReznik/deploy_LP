from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Courses, News, Category


class CoursesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        
        
class NewsSerializer(HyperlinkedModelSerializer):
    class Meta: 
        model = News
        fields = '__all__'
        
        
class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'