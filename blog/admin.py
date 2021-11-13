from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blog.models import Post, PostTag, ForeignPost


class ForeignPostInline(admin.TabularInline):
    model = ForeignPost
    fk_name = 'parent'


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    filter_horizontal = ('tags',)
    inlines = [ForeignPostInline]
