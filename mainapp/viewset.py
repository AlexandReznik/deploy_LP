from rest_framework.viewsets import ModelViewSet
from .serializers import (
    CoursesSerializer, 
    NewsSerializer, 
    CategorySerializer, 
    LessonSerializer, 
    CourseFeedbackSerializer, 
    CourseTeacherSerializer, 
    SubscribtionSerializer
    )
from .models import (
    Courses,
    News, 
    Category, 
    Lesson, 
    CourseFeedback, 
    Subscription, 
    CourseTeacher
    )
from .filters import NewsFilter, CoursesFilter, CourseTeacherFilter, LessonFilter
from rest_framework.pagination import LimitOffsetPagination
from .permissions import ReadOnly


class LimitPagination(LimitOffsetPagination):
    default_limit = 10
    
    
class CoursesViewSet(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    filterset_class = CoursesFilter
    pagination_class = LimitPagination
    permission_classes = [ReadOnly]
    

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filterset_class = NewsFilter
    pagination_class = LimitPagination
    permission_classes = [ReadOnly]
    

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnly]
    
    
class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filterset_class = LessonFilter
    pagination_class = LimitPagination
    permission_classes = [ReadOnly]
    
    
class CourseTeacherViewSet(ModelViewSet):
    queryset = CourseTeacher.objects.all()
    serializer_class = CourseTeacherSerializer
    filterset_class = CourseTeacherFilter
    permission_classes = [ReadOnly]
    
    
class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscribtionSerializer
    pagination_class = LimitPagination
    permission_classes = [ReadOnly]
    
    
class CourseFeedbackViewSet(ModelViewSet):
    queryset = CourseFeedback.objects.all()
    serializer_class = CourseFeedbackSerializer
    pagination_class = LimitPagination
    permission_classes = [ReadOnly]
    