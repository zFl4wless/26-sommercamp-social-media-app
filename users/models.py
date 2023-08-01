from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

