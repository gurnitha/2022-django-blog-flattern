# apps/blog/urls.py

# Django module
from django.urls import path

# Locals
from apps.blog.views import *

app_name = 'blog'

urlpatterns = [
    path('posts/', posts, name='posts'),
]

