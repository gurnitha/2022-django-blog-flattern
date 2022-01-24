# apps/portfolio/models.py

# Django modules
from django.db import models

# Locals

# Create your models here.


# Model: Slider
class Slider(models.Model):
	slider_title1 = models.CharField(max_length=150, blank=True, null=True)
	slider_title2 = models.CharField(max_length=150, blank=True, null=True)
	slider_sub_title = models.CharField(max_length=200)
	slider_thumbnail = models.ImageField(upload_to='sliders/%Y/%m/%d/', blank=False)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Slider'
		verbose_name_plural = 'Sliders'


	def __str__(self):
		return self.slider_title1


# Model: Services
class Service(models.Model):
	service_icon = models.CharField(max_length=50)
	service_title = models.CharField(max_length=150) 
	service_description = models.CharField(max_length=200) 
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name = 'Service'
		verbose_name_plural = 'Services'


	def __str__(self):
		return self.service_title