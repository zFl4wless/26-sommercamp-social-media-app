from PIL import Image
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    image = models.ImageField(default='default.png', upload_to="uploads")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

