from datetime import timezone

from django.db import models
from django.contrib.auth.models import User

from blog.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, default=None)

    def __str__(self):
        return self.content
