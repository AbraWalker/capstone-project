from django.contrib import admin
from .models import Post, Guide
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('game_title', 'author')
    search_fields = ['title']
    summernote_fields = ('content',)

@admin.register(Guide)
class GuideAdmin(SummernoteModelAdmin):
    list_display = ('game_title', 'author')
