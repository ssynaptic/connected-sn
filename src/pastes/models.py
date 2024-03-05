from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

from django.db import models
from django.contrib.auth.models import AbstractUser

class Paste(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(max_length=5000, blank=False, null=False)
    publish_date = models.DateField(auto_now_add=True, blank=False, null=False)
    last_updated = models.DateField(auto_now=True, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=False, null=False)
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paste = models.ForeignKey(Paste, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True, blank=False, null=False)
    content = models.TextField(max_length=3000, blank=False, null=False)

    def __str__(self):
        return self.user.username

class PasteView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paste = models.ForeignKey(Paste, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paste = models.ForeignKey(Paste, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paste = models.ForeignKey(Paste, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username