from mainapp import views
from django.urls import path
from mainapp.apps import MainappConfig
from django.views.decorators.cache import cache_page

app_name = MainappConfig.name

urlpatterns = [
    path('contacts/', views.ContactsView.as_view(), name="contacts"),
    path('docs/', views.DocSitePageView.as_view(), name="docs"),
    path('', views.MainPageView.as_view(), name="mainapp"),

    # News
    path("news/", views.NewsListView.as_view(), name="news"),
    path("news/create/", views.NewsCreateView.as_view(), name="news_create",),
    path("news/<int:pk>/detail",views.NewsDetailView.as_view(),name="news_detail",),
    path("news/<int:pk>/update",views.NewsUpdateView.as_view(),name="news_update",),
    path("news/<int:pk>/delete",views.NewsDeleteView.as_view(),name="news_delete",),

    # Courses
    path("courses/", cache_page(60 * 5)(views.CourseListView.as_view()), name="courses"),
    path("courses/<int:pk>/detail/", views.CourseDetailView.as_view(), name="courses_detail",),
    path("course_feedback/", views.CourseFeedbackFormProcessView.as_view(), name="course_feedback",),
    path("course_signup/", views.create_subscription, name="course_signup"),
    path('my_courses/', views.MyCoursesView.as_view(), name="my_courses"),
    path("mycourse/<int:pk>/detail/", views.MyCourseDetailView.as_view(), name="mycourse_detail"),
    path('mycourse/<int:pk>/delete', views.MyCourseDeleteView.as_view(), name="mycourse_delete"),

    # Teacher
    path("teacher/<int:pk>/detail", views.TeacherDetailView.as_view(), name="teacher_detail"),
    
    # Logs
    path('logs/', views.LogView.as_view(), name='log_view'),
    path("log_download/", views.LogDownloadView.as_view(), name="log_download"),
    
    # Categories
    path('course-by-category/', views.CourseListByCategoriesView.as_view(), name='categories'),

    # Other
    path('success/', views.SuccessView.as_view(), name="success"),
    path('error/', views.ErrorView.as_view(), name='error'),
]
