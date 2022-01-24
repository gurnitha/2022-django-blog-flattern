# apps/blog/templates/blog/posts.html

# Django modules
from django.shortcuts import render

# Create your views here.


# Post view
def posts(request):
	return render(request, 'blog/posts.html')


# Single view
def single(request):
	return render(request, 'blog/single.html')
