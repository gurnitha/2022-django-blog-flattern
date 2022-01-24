# apps/blog/templates/blog/posts.html

# Django modules
from django.shortcuts import render

# Create your views here.


# Homepage view
def posts(request):
	return render(request, 'blog/posts.html')
