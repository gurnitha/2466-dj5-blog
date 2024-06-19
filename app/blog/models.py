# src/app/blog/models.py

# Django and third parties modules
from django.db import models
# from django.utils import timezone
from django.db.models.functions import Now

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250)
	body = models.TextField()
	# publish = models.DateTimeField(default=timezone.now)
	publish = models.DateTimeField(db_default=Now())

	def __str__(self):
		return self.title