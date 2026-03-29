from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post
from django.http import HttpRequest

def post_list(request: HttpRequest):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request=request, template_name='post_list.html', context=context)


def post_detail(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request=request, template_name='post_detail.html', context=context)

def author_post_list(request: HttpRequest, author_pk: int):
    posts = get_list_or_404(Post, author=author_pk)  # Post.objects.filter(author=author_pk)
    context = {
        'posts': posts,
    }
    return render(request=request, template_name='post_list.html', context=context)