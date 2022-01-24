# apps/portfolio/templates/portfolio/index.html

# Django modules
from django.shortcuts import render

# Locals
from apps.portfolio.models import Slider, Service

# Create your views here.


# Homepage view
def index(request):
	sliders = Slider.objects.order_by('-id')[0:3]
	services = Service.objects.order_by('id')[0:4]
	context = {'sliders':sliders, 'services':services}
	return render(request, 'portfolio/index.html', context)

# Porpolio view
def portfolio(request):
	return render(request, 'portfolio/portfolio.html')