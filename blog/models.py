from typing import Iterable

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40, unique=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = CKEditor5Field(
        'Conteúdo',
        config_name='default',
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    featured_image = models.ImageField(upload_to='posts/')
    is_tutorial = models.BooleanField(default=False)
    github_link = models.URLField(blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_rendered_content(self):
        """Método auxiliar para renderizar Markdown -> HTML no template"""
        import markdown
        return markdown.markdown(
            self.content,
            extensions=[
                'markdown.extensions.extra',         # tables, fenced code, etc
                'markdown.extensions.codehilite',    # ou use pygments
                'markdown.extensions.toc',
                'markdown.extensions.sane_lists',
            ],
            extension_configs={
                'markdown.extensions.codehilite': {
                    'linenums': False,          # linhas numeradas (opcional)
                    'guess_lang': True,         # tenta detectar linguagem
                    'use_pygments': True,       # usa Pygments (ESSENCIAL)
                    'pygments_style': 'dracula' # 🎨 tema de cores
                }
            }
        )
