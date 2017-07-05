from django.db import models

# Create your models here.

# Post
class post(models.Model):
    quote = models.CharField(max_length=255)
    author = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.quote