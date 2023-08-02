from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from blog.models import Post
from likes.models import Like
from .models import Comment


def send_comment(request):

    if request.method == 'POST':

        # comment_form = CommentForm(request.POST)
        content = request.POST.get('content')
        post_id = request.POST.get("post_id")
        post_author = request.POST.get("post_author")

        post = Post.objects.get(id=post_id)
        author = User.objects.get(id=post_author)

        #if comment_form.is_valid():
        #    comment_form.save()
        comment = Comment(content=content, author=author, post=post)

        comment.save()




    context = {
        'posts': Post.objects.all(),
        'likes': Like.objects.all(),
        'comments': Comment.objects.all(),
    }

    return redirect('/')