from django import forms
from .models import Comment, Raitingstar, Raiting

class ReviewForm(forms.ModelForm):
    '''Форма отзывов'''

    class Meta:
        model = Comment
        fields = ("name", "email", "text")

class RaitingForm(forms.ModelForm):
    '''Форма добавления рейтинга'''
    star = forms.ModelChoiceField(
        queryset=Raitingstar.objects.all(), widget=forms.RadioSelect(), empty_label=None
        )
    class Meta:
        model = Raiting
        fields = ("star",)