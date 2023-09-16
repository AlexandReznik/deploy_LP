from rest_framework.serializers import HyperlinkedModelSerializer
from .models import (
    Courses,
    News, 
    Category, 
    Lesson, 
    CourseFeedback, 
    Subscription, 
    CourseTeacher
    )


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
        

class LessonSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        
        
class CourseTeacherSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CourseTeacher
        fields = '__all__'
        
        
class CourseFeedbackSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CourseFeedback
        fields = '__all__'
        

class SubscribtionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'