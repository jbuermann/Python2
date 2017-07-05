from django.db import models
from datetime import datetime


# Create your models here.
class post_authors(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Post
class post(models.Model):
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=255,blank=True)
    banner = models.ImageField(upload_to='images/banners',blank=True)
    author = models.ForeignKey(post_authors, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    timestamp = models.DateTimeField('Creation Date', default=datetime.now)
    TYPE_CHOICE = (
        (1, 'Page'),# Included in menu
        (2, 'Article'),# Listed on articles page
    )
    type = models.IntegerField(choices=TYPE_CHOICE, default=1)

    def __str__(self):
        return self.title