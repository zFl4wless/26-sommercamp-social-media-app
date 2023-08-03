from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect

from blog.models import Post
from dislikes.models import Dislike
from likes.models import Like


def dislike_post(request):
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

        user_disliked = Dislike.objects.filter(post=post, author=user)
        if user_disliked.exists():
            user_disliked.delete()
            return redirect(request.META['HTTP_REFERER'])

        user_liked = Like.objects.filter(post=post, author=user)
        if user_liked.exists():
            user_liked.delete()

        Dislike.objects.create(post=post, author=user)

        return redirect(request.META['HTTP_REFERER'])
