from django.contrib.auth.models import User
from django.shortcuts import redirect

from blog.models import Post
from .models import Comment


def send_comment(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        post_id = request.POST.get("post_id")
        post_author = request.POST.get("post_author")

        post = Post.objects.get(id=post_id)
        author = User.objects.get(id=post_author)

        comment = Comment(content=content, author=author, post=post)

        comment.save()

        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('/')