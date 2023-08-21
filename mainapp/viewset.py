from rest_framework.viewsets import ModelViewSet
from .serializers import CoursesSerializer, NewsSerializer, CategorySerializer
from .models import Courses, News, Category
from .filters import NewsFilter, CoursesFilter
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