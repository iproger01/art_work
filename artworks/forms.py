from django import forms
from .models import Comment

class ReviewForm(forms.ModelForm):
    '''Форма отзывов'''

    class Meta:
        model = Comment
        fields = ("name", "email", "text")

