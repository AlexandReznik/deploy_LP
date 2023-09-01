from authapp import views
from django.urls import path
from authapp.apps import AuthappConfig
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = AuthappConfig.name


urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("profile_edit/<int:pk>/", views.ProfileEditView.as_view(), name="profile_edit"),
    path("mytoken/", views.get_token, name="mytoken"),
    path("api-guide/", views.TokenView.as_view(), name="api_guide"),
    path('password-reset/', PasswordResetView.as_view(template_name='authapp/password_reset.html', html_email_template_name='authapp/password_reset_email.html', subject_template_name = 'authapp/password_reset_subject'),name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='authapp/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='authapp/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='authapp/password_reset_complete.html'),name='password_reset_complete'),
]
