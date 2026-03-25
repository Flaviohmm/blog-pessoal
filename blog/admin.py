from django.contrib import admin
from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Post, Category, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)                    # Removido prepopulated_fields
    # Se quiser slug no Tag no futuro, adicione o campo no model primeiro


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_tutorial', 'published_at', 'views')
    list_filter = ('category', 'is_tutorial', 'published_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    
    # Configuração do CKEditor 5
    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }