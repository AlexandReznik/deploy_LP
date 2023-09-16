from rest_framework.viewsets import ModelViewSet
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.pagination import LimitOffsetPagination
from .permissions import StaffOnly
from .filters import CustomUserFilter


class LimitPagination(LimitOffsetPagination):
    default_limit = 20

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    pagination_class = LimitPagination
    filterset_class = CustomUserFilter
    permission_classes = [StaffOnly]