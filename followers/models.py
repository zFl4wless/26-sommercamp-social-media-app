from django.contrib.auth.models import User
from django.db import models


class Follower(models.Model):
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_user')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
