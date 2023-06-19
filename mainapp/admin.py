from django.contrib import admin
from mainapp.models import News, Courses, Lesson, CourseTeacher
from django.utils.translation import gettext_lazy as _


admin.site.register(Courses)
admin.site.register(CourseTeacher)

@admin.site.register(Courses)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    list_per_page = 5
    ordering = ['-num']
    list_filter = ['created_at', 'course', 'deleted']
    search_fields = ['title', 'created_at']
    actions = ['mark_deleted']

    def get_course_name(self, obj):
        return obj.course.title

    get_course_name.short_description = _("Course")

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    search_fields = ['title', 'preamble', 'body']
    list_filter = ['created_at']
    actions = ['mark_deleted']

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")
