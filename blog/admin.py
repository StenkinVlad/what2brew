from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    # summernote_fields = '__all__'

admin.site.register(Post, PostAdmin)


