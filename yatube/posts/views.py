from django.shortcuts import get_object_or_404, render

from .const import POST_COUNT
from .models import Group, Post


def index(request):
    """Функция обрабатывает запросы к главной странице,
    получает данные из модели Post и связанной модели Group,
    выводит 10 последних постов и рендерит их в шаблон."""
    posts = Post.objects.select_related('group', 'author')[:POST_COUNT]
    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Функция обрабатывает запросы к странице с публикациями группы,
    получает группу из модели и проверяет url к ней компановщиком slug,
    собирает словарь из данных и рендерит их в шаблон."""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')[:POST_COUNT]
    context = {
        'group': group,
        'posts': posts
    }

    return render(request, 'posts/group_list.html', context)
