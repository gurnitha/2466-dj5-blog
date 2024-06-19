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
	post = get_object_or_404(
		Post,
		id=id,
		status=Post.Status.PUBLISHED
	)
	data = {
		'post': post
	}
	return render(request, 'blog/post/detail.html', data)