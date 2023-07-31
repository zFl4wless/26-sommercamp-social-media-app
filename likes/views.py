from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Post
from likes.models import Like


def like_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        user_id = request.POST.get('user_id')

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return HttpResponse("Invalid post_id. Post does not exist.")

        try:
            user = User.objects.get(pk=user_id)
        except Post.DoesNotExist:
            return HttpResponse("Invalid user_id. User does not exist.")

        if Like.objects.filter(post=post, author=user).exists():
            Like.objects.filter(post=post, author=user).delete()
            return redirect(request.META['HTTP_REFERER'])

        Like.objects.create(post=post, author=user)

        return redirect(request.META['HTTP_REFERER'])
