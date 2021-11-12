from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blog.models import Post, PostTag


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    filter_horizontal = ('tags',)
