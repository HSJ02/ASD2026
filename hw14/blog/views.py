from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag


class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/post_list.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


def study_page(request):
    return render(request, 'blog/study.html')


def insight_page(request):
    return render(request, 'blog/insight.html')


def dailylife_page(request):
    return render(request, 'blog/dailylife.html')


def project_page(request):
    return render(request, 'blog/project.html')


def category_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    post_list = Post.objects.filter(category=category).order_by('-pk')

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'category': category,
        }
    )

def tag_page(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    post_list = Post.objects.filter(tags=tag).order_by('-pk')

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'tag': tag,
        }
    )