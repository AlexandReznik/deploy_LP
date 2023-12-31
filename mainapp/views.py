from multiprocessing import context
from tempfile import template
from django.http import HttpResponse, FileResponse
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView
from mainapp import tasks as mainapp_tasks
from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.http import JsonResponse
from authapp import models as authapp_models
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View
)
from config import settings
from mainapp import models as mainapp_models
from mainapp import forms as mainapp_forms
import logging
logger = logging.getLogger(__name__)


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class SuccessView(TemplateView):
    template_name = "mainapp/succsess.html"


class ErrorView(TemplateView):
    template_name = "mainapp/error.html"


class NewsListView(ListView):
    template_name = 'mainapp/news_list.html'
    model = mainapp_models.News
    paginate_by = 5
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset().filter(deleted=False)
        min_date = self.request.GET.get('min_date')
        max_date = self.request.GET.get('max_date')

        if min_date:
            queryset = queryset.filter(created_at__gte=min_date)
        if max_date:
            queryset = queryset.filter(created_at__lte=max_date)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_date_form'] = mainapp_forms.DateFilterForm(self.request.GET)
        return context


class NewsCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'mainapp/news_form.html'
    model = mainapp_models.News
    fields = "__all__"

    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.add_news",)


class NewsDetailView(DetailView):
    template_name = 'mainapp/news_detail.html'
    model = mainapp_models.News


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'mainapp/news_form.html'
    model = mainapp_models.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.change_news",)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'mainapp/news_confirm_delete.html'
    model = mainapp_models.News
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.delete_news",)


class CourseListView(ListView):
    template_name = "mainapp/courses_list.html"
    model = mainapp_models.Courses
    paginate_by = 5
    context_object_name = 'courses'
    ordering = ['-created_at']
        
    def get_queryset(self):
        queryset = super().get_queryset().filter(deleted=False)
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        category = self.request.GET.getlist('category')

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if category:
            queryset = queryset.filter(category__in=category)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = mainapp_forms.PriceFilterForm(self.request.GET)
        return context

class CourseDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        logger.debug("Yet another log message")
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(
            mainapp_models.Courses, pk=pk
        )
        context["teachers"] = mainapp_models.CourseTeacher.objects.filter(
            courses=context["course_object"]
        )
        if not self.request.user.is_anonymous:
            if not mainapp_models.CourseFeedback.objects.filter(
                course=context["course_object"], user=self.request.user
            ).count():
                context["feedback_form"] = mainapp_forms.CourseFeedbackForm(
                    course=context["course_object"], user=self.request.user
                )
        context["feedback_list"] = mainapp_models.CourseFeedback.objects.filter(
            course=context["course_object"]).order_by("-created", "-rating")[:5]

        cached_feedback = cache.get(f"feedback_list_{pk}")
        if not cached_feedback:
            context["feedback_list"] = mainapp_models.CourseFeedback.objects.filter(
                course=context["course_object"]).order_by("-created", "-rating")[:5].select_related()
            cache.set(f"feedback_list_{pk}",
                      context["feedback_list"], timeout=300)
        else:
            context['feedback_list'] = cached_feedback

        if context["course_object"].price is not None and context["course_object"].discount is not None:
            discount_price = context["course_object"].price - (
                (context["course_object"].price * context["course_object"].discount) / 100)
            context["discount_price"] = discount_price
        return context


def create_subscription(request):
    if request.method == 'POST':
        form = mainapp_forms.SubscriptionForm(request.POST)

        if form.is_valid():
            course = form.cleaned_data['course']
            if mainapp_models.Subscription.objects.filter(user=request.user, course=course).exists():
                return redirect('mainapp:error')
            else:
                subscription = form.save(commit=False)
                subscription.user = request.user
                subscription.save()
                return redirect('mainapp:success')
    else:
        form = mainapp_forms.SubscriptionForm()
    return render(request, 'mainapp/course_subscription.html', {'form': form})


class MyCoursesView(ListView):
    template_name = 'mainapp/course_user.html'
    model = mainapp_models.Subscription
    context_object_name = 'my_courses'

    def get_queryset(self):
        return mainapp_models.Subscription.objects.filter(user=self.request.user)


class MyCourseDetailView(TemplateView):
    template_name = 'mainapp/course_lessons.html'
    
    def get_context_data(self, pk=None, **kwargs):
        context = super(MyCourseDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(
            mainapp_models.Courses, pk=pk
        )
        context["lessons"] = mainapp_models.Lesson.objects.filter(
            course=context["course_object"]
        )
        context["teachers"] = mainapp_models.CourseTeacher.objects.filter(
            courses=context["course_object"]
        )
        return context
    
    
class MyCourseDeleteView(DeleteView):
    template_name = 'mainapp/mycourse_confirm_delete.html'
    model = mainapp_models.Subscription
    success_url = reverse_lazy("mainapp:my_courses")
    

class CourseFeedbackFormProcessView(LoginRequiredMixin, CreateView):
    model = mainapp_models.CourseFeedback
    form_class = mainapp_forms.CourseFeedbackForm

    def form_valid(self, form):
        self.object = form.save()
        rendered_card = render_to_string(
            "mainapp/includes/feedback_card.html", context={"item": self.object}
        )
        return JsonResponse({"card": rendered_card})


class CourseListByCategoriesView(View):
    def get(self, request):
        categories = mainapp_models.Category.objects.all()
        selected_category_id = request.GET.get('category')
        if selected_category_id:
            courses = mainapp_models.Courses.objects.filter(
                category_id=selected_category_id)
        else:
            courses = mainapp_models.Courses.objects.all()
        context = {
            'categories': categories,
            'courses': courses,
            'selected_category_id': selected_category_id,
        }
        return render(request, 'mainapp/course_by_category.html', context)


class TeacherDetailView(DetailView):
    template_name = 'mainapp/teacher.html'
    model = mainapp_models.CourseTeacher
    
    
class LogView(TemplateView):
    template_name = "mainapp/log_view.html"

    def get_context_data(self, **kwargs):
        context = super(LogView, self).get_context_data(**kwargs)
        log_slice = []
        with open(settings.LOG_FILE, "r") as log_file:
            for i, line in enumerate(log_file):
                if i == 1000:
                    break
                log_slice.insert(0, line)
            context["log"] = "".join(log_slice)
        return context


class LogDownloadView(UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, *args, **kwargs):
        return FileResponse(open(settings.LOG_FILE, "rb"))


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    