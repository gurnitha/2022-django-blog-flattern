# apps/portfolio/templates/portfolio/index.html

# Django modules
from django.shortcuts import render

# Locals
from apps.portfolio.models import Slider, Service, Gallery, Client, Category

# Create your views here.


# Homepage view
def index(request):
	sliders = Slider.objects.order_by('-id')[0:3]
	services = Service.objects.order_by('id')[0:4]
	galleries = Gallery.objects.order_by('-id')[0:8]
	clients = Client.objects.order_by('-id')[0:12]
	context = {
		'sliders':sliders, 
		'services':services,
		'galleries':galleries,
		'clients':clients
	}
	return render(request, 'portfolio/index.html', context)

# Porpolio view
def portfolio(request):
	categories = Category.objects.all()
	galleries  = Gallery.objects.order_by('-id')[0:8]
	galleries_web  = Gallery.objects.filter(is_galery_data_type_web=True)
	galleries_icon  = Gallery.objects.filter(is_galery_data_type_icon=True)
	galleries_graphic  = Gallery.objects.filter(is_galery_data_type_graphic=True)
	galleries_webdev  = Gallery.objects.filter(is_galery_data_type_graphic=True)
	context = {
		'categories':categories,
		'galleries':galleries,
		'galleries_web':galleries_web,
		'galleries_icon':galleries_icon,
		'galleries_graphic':galleries_graphic,
		'galleries_webdev':galleries_webdev,
	}
	return render(request, 'portfolio/portfolio.html', context)