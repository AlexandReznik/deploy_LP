from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from pathlib import Path
from time import time
from django.core.validators import MaxValueValidator
from authapp import models as authapp_models


def course_avatars_path(instance, filename):
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return "course_{0}/avatars/{1}".format(instance.id, f"pic_{num}{suff}")


class News(models.Model):
    title = models.CharField(max_length=256)
    preamble = models.CharField(max_length=1024)
    body = models.TextField()
    body_as_markdown = models.BooleanField(
        default=False)

    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        

class CoursesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class Courses(models.Model):
    objects = CoursesManager()
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    discount = models.IntegerField(validators=[MaxValueValidator(100)], null=True, default=None, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    avatar = models.ImageField(
        upload_to=course_avatars_path, blank=True, null=True
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=None, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class Subscription(models.Model):
    user = models.ForeignKey(authapp_models.CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    

class Lesson(models.Model):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=256)
    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class CourseTeacher(models.Model):
    courses = models.ManyToManyField(Courses)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    about = models.TextField(default="", null=True, blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class CourseFeedback(models.Model):
    RATING = (
        (5, "⭐⭐⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (3, "⭐⭐⭐"),
        (2, "⭐⭐"),
        (1, "⭐")
    )
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE, verbose_name=_("Course")
    )
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name=_("User")
    )
    feedback = models.TextField(
        default=_("No feedback"), verbose_name=_("Feedback")
    )
    rating = models.SmallIntegerField(
        choices=RATING, default=5, verbose_name=_("Rating")
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course} ({self.user})"
