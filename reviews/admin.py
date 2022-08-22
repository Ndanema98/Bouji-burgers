from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title','slug','status','created_on')
    search_fields = ['title','content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status','created_on')
    summernote_fields = ('content',)
    actions = ['approve_post']

    def approve_post(self, request, queryset):
        queryset.update(approved=True)




