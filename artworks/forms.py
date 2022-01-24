from django import forms
from .models import Comment, Raitingstar, Raiting
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

class ReviewForm(forms.ModelForm):
    '''Форма отзывов'''
    captcha = ReCaptchaField()
    class Meta:
        model = Comment
        fields = ("name", "email", "text", "captcha")
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control border"}),
            "email":forms.EmailInput(attrs={"class":"form-control border"}),
            "text":forms.Textarea(attrs={"class":"form-control border"})
        }

class RaitingForm(forms.ModelForm):
    '''Форма добавления рейтинга'''
    star = forms.ModelChoiceField(
        queryset=Raitingstar.objects.all(), widget=forms.RadioSelect(), empty_label=None
        )
    class Meta:
        model = Raiting
        fields = ("star",)