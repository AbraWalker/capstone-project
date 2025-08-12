from .models import Post
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('game_title','content','rating',)