from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django import forms

from blog.models import Post
from .models import Comment


def send_comment(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        post_id = request.POST.get("post_id")
        comment_author = request.POST.get("comment_author")

        post = Post.objects.get(id=post_id)
        author = User.objects.get(id=comment_author)

        comment = Comment(content=content, author=author, post=post)

        comment.save()

        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('/')


def delete_comment(request):
    if request.method == 'POST':
        comment_id = int(request.POST.get('comment_id'))
        user_id = int(request.POST.get('user_id'))
        post_author_id = int(request.POST.get('post_author_id'))

        if user_id == Comment.objects.get(id=comment_id).author_id or user_id == post_author_id:

            entry = Comment.objects.get(id=comment_id)
            entry.delete()

            messages.success(request, 'Comment deleted')
            return redirect('/')

        else:
            return redirect('/')

    else:
        return redirect('/')


def edit_comment(request, pk):

    comment_form = CommentForm(request.POST, instance=request.content)
    comment_id = pk

    entry = Comment.objects.get(id=comment_id)
    entry.content = comment_form['content']
    entry.save()

    return render(request, 'comment/update_comment.html', {"comment_form": comment_form})


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
