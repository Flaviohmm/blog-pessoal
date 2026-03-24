from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')}
    }
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'published_at', 'category')