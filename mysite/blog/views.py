
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post/detail.html'