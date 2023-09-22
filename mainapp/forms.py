from django import forms
from django.utils.translation import gettext_lazy as _
from mainapp import models as mainapp_models
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class SubscriptionForm(forms.ModelForm):
    def __init__(self, *args, course=None, user=None, **kwargs):
        ret = super().__init__(*args, **kwargs)
        if course and user:
            self.fields["course"].initial = course.pk
            self.fields["user"].initial = user.pk
        return ret
    
    class Meta:
        model = mainapp_models.Subscription
        fields = ['course', 'captcha']
        
        widgets = {
            "course": forms.RadioSelect(),
        }
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
        
        
class CourseFeedbackForm(forms.ModelForm):
    def __init__(self, *args, course=None, user=None, **kwargs):
        ret = super().__init__(*args, **kwargs)
        if course and user:
            self.fields["course"].initial = course.pk
            self.fields["user"].initial = user.pk
        return ret

    class Meta:
        model = mainapp_models.CourseFeedback
        fields = ("course", "user", "feedback", "rating", "captcha")
        widgets = {
            "course": forms.HiddenInput(),
            "user": forms.HiddenInput(),
            "rating": forms.RadioSelect(),
        }
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    
    
class PriceFilterForm(forms.Form):
    min_price = forms.DecimalField(required=False, min_value=0)
    max_price = forms.DecimalField(required=False, min_value=0)
    category = forms.ModelMultipleChoiceField(required=False, queryset=mainapp_models.Category.objects.all(), widget=forms.CheckboxSelectMultiple)
