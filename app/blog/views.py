# src/app/blog/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals
from app.blog.models import Post

# Create your views here.

def post_list(request):
	posts = Post.published.all()
	data = {
		'posts': posts
	}
	return render(request,'blog/post/list.html', data)


def post_detail(request, id):
	try:
		post = Post.published.get(id=id)
	except Post.DoesNotExist:
		raise Http404("No Post found.")
	data = {
		'post': post
	}
	return render(request,blog/post/detail.html', data)