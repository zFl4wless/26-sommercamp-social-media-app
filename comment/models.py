from django.db import models
from django.contrib.auth.models import User

from blog.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.content
