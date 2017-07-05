from django.contrib import admin
from .models import post,post_authors
# Register your models here.
admin.site.register(post)
admin.site.register(post_authors)
