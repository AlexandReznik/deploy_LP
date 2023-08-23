"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from rest_framework.routers import DefaultRouter
from mainapp.viewset import CategoryViewSet, NewsViewSet, CoursesViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views
from rest_framework import permissions


router = DefaultRouter()
router.register('courses', CoursesViewSet)
router.register('categories', CategoryViewSet)
router.register('news', NewsViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="sashaaaareznik@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticatedOrReadOnly],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='mainapp/')),
    path('mainapp/', include('mainapp.urls', namespace='mainapp')),
    path('authapp/', include('authapp.urls', namespace='authapp')),
    path('social_auth/', include('social_django.urls', namespace='social')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
] 

urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
