from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


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