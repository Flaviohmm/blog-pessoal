from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

class Tag(models.Model):
    name = models.CharField(max_length=30)

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
        )
