from django.contrib import admin
from .models import Post, UserVotes
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('game_title', 'author')
    search_fields = ['title']
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(UserVotes)