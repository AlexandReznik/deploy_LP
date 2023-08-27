from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm
import os
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox


class CustomUserCreationForm(UserCreationForm):
    mycaptcha = CaptchaField()
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "age",
            "avatar",
            "captcha",
        )
    field_classes = {"username": UsernameField}

    def clean_age(self):
        data = self.cleaned_data.get("age")
        if data > 100:
            raise ValidationError(_("Please, enter a valid age!"))
        return data


class CustomUserChangeForm(UserChangeForm):
    mycaptcha = CaptchaField()
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "age",
            "avatar",
            "captcha",
        )
    field_classes = {"username": UsernameField}

    def clean_avatar(self):
        arg_as_str = "avatar"
        if arg_as_str in self.changed_data and self.instance.avatar:
            if os.path.exists(self.instance.avatar.path):
                os.remove(self.instance.avatar.path)
        return self.cleaned_data.get(arg_as_str)

    def clean_age(self):
        data = self.cleaned_data.get("age")
        if data is not None and data > 100:
            raise ValidationError(_("Please, enter a valid age!"))
        return data
