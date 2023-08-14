from django import forms
from django.utils.translation import gettext_lazy as _
from mainapp import models as mainapp_models
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox
# from captcha.fields import CaptchaField

class SubscriptionForm(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    def __init__(self, *args, course=None, user=None, **kwargs):
        ret = super().__init__(*args, **kwargs)
        if course and user:
            self.fields["course"].initial = course.pk
            self.fields["user"].initial = user.pk
        return ret
    
    class Meta:
        model = mainapp_models.Subscription
        fields = ['course']
        
        widgets = {
            "course": forms.RadioSelect(),
        }
        
        
class CourseFeedbackForm(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    def __init__(self, *args, course=None, user=None, **kwargs):
        ret = super().__init__(*args, **kwargs)
        if course and user:
            self.fields["course"].initial = course.pk
            self.fields["user"].initial = user.pk
        return ret

    class Meta:
        model = mainapp_models.CourseFeedback
        fields = ("course", "user", "feedback", "rating")
        widgets = {
            "course": forms.HiddenInput(),
            "user": forms.HiddenInput(),
            "rating": forms.RadioSelect(),
        }
