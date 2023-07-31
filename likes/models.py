from django.contrib.auth.models import User
from django.db import models

from blog.models import Post


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
