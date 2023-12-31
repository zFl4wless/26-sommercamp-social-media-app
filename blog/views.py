from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from comment.models import Comment
from followers.models import Follower
from likes.models import Like
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
        'likes': Like.objects.all(),
        'comments': Comment.objects.all()
    }

    return render(request, 'blog/home.html', context)


def search(request):
    template = 'blog/home.html'

    query = request.GET.get('q')

    result = Post.objects.filter(
        Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query) | Q(
            tags__name__icontains=query)).distinct()

    context = {'posts': result}
    return render(request, template, context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


def followed_user_posts(request):
    def map_follower(follower):
        return follower[0]

    follower_ids = list(map(map_follower, Follower.objects.filter(follower=request.user).values_list('followed_user')))
    posts = Post.objects.filter(author__in=User.objects.filter(id__in=follower_ids)).order_by('-date_posted')

    return render(request, 'blog/home.html', {'posts': posts})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'file', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'file', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'about.html', {'title': 'About'})


def privacypolicy(request):
    return render(request, 'privacy-policy.html', {'title': 'Privacy Policy'})

def imprint(request):
    return render(request, 'imprint.html', {'title': 'Imprint'})
