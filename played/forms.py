from .models import Post, Guide
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('game_title', 'slug', 'content','overall_rating', 'difficulty_rating', 'value_rating')

class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ('game_title', 'content', 'completed')