from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blog.models import Post, PostTag, ForeignPost, Volunteer


class ForeignPostInline(admin.TabularInline):
    model = ForeignPost
    fk_name = 'parent'


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    pass

@admin.register(Volunteer)
class VolunteerAdmin(SummernoteModelAdmin):
    summernote_fields = ['description']

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ['body']
    filter_horizontal = ('tags',)
    inlines = [ForeignPostInline]
