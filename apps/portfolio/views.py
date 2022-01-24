# apps/portfolio/templates/portfolio/index.html

# Django modules
from django.shortcuts import render

# Create your views here.


# Homepage view
def index(request):
	return render(request, 'portfolio/index.html')