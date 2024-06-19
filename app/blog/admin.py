# src/app/blog/admin.py

# Django and third parties modules
from django.contrib import admin

# Register your models here.

from app.blog.models import Post

admin.site.register(Post)