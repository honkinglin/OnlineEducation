from django import forms

from apps.operation.models import UserAsk
from captcha.fields import CaptchaField

class UserAskForm(forms.Form):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']