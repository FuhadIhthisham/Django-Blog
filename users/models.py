from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile pic')
    bio = models.TextField(default='', max_length=300, blank=True)
    instagram_url = models.URLField(max_length=255, default='', blank=True)
    fb_url = models.URLField(max_length=255, blank=True)
    linkedin_url = models.URLField(max_length=255, blank=True)
    website_url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.width > 300 or img.height > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)