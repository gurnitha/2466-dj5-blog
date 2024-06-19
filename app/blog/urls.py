# config/urls.py

# Django and third parties modules
from django.urls import path

# Locals
from app.blog import views

app_name = 'blog'

urlpatterns = [
	# post views
	path('', views.post_list, name='post_list'),
	path('<int:id>/', views.post_detail, name='post_detail'),
]
