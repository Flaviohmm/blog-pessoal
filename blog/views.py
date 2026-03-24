from typing import Any, cast

from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Count
from django.shortcuts import render
from .models import Post, Category, Tag


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.filter().order_by('-published_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Incrementa views (simples, sem cache por enquanto)
        obj = cast(Post, obj)
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        obj = self.get_object()

        context['related_posts'] = Post.objects.filter(
            category=obj.category
        ).exclude(pk=obj.pk).order_by('-published_at')[:4]

        return context
            

class CategoryDetailView(ListView):
    template_name = 'blog/category_detail.html'
    context_object_name = 'posts'
    paginate_by = 12

    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.filter(
            category__slug=self.kwargs['slug']
        ).order_by('-published_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context
    

class TagDetailView(ListView):
    template_name = 'blog/tag_detail.html'
    context_object_name = 'posts'
    paginate_by = 12

    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.filter(
            tags__slug=self.kwargs['slug']
        ).order_by('-published_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context
    

class TutorialListView(ListView):
    model = Post
    template_name = 'blog/tutorial_list.html'
    context_object_name = 'tutorials'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.filter(is_tutorial=True).order_by('-published_at')
    

class PortfolioView(TemplateView):
    template_name = 'blog/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Você pode puxar repositórios via Github API ou deixar estático
        context['projects'] = [
            {'name': 'Blog Pessoal', 'url': 'https://github.com/seuuser/blog-pessoal', 'desc': 'Este blog feito em Django + Tailwind'}
        ]
        return context