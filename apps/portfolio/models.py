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


# Model: Galery Category
class Category(models.Model):
	category_name = models.CharField(max_length=50, blank=True, null=True)
	category_class_name = models.CharField(max_length=50, blank=True, null=True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'


	def __str__(self):
		return self.category_name

# Model: Services
class Gallery(models.Model):

	DATA_TYPE_CHOICES = [
		('webdesign', 'webdesign'),
		('webdev', 'webdev'),
		('icon', 'icon'),
		('graphic', 'graphic'),
	]

	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
	gallery_image_full = models.ImageField(upload_to='gallery/%Y/%m/%d/', blank=False)
	gallery_thumbnail = models.ImageField(upload_to='gallery/%Y/%m/%d/', blank=False)
	gallery_image_title = models.CharField(max_length=200) 
	gallery_image_description = models.CharField(max_length=200) 
	gallery_data_type = models.CharField(max_length=30, choices=DATA_TYPE_CHOICES, default='webdesign')
	# is_galery_data_type_web = models.BooleanField(blank=True, null=True)
	# is_galery_data_type_icon = models.BooleanField(blank=True, null=True)
	# is_galery_data_type_graphic = models.BooleanField(blank=True, null=True)
	# is_galery_data_type_webdev = models.BooleanField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name = 'Gallery'
		verbose_name_plural = 'Galleries'


	def __str__(self):
		return self.gallery_image_title


# Model: Client
class Client(models.Model):
	client_company_logo = models.ImageField(upload_to='client/%Y/%m/%d/', blank=False)
	client_company_name = models.CharField(max_length=150)  
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name = 'Client'
		verbose_name_plural = 'Clients'


	def __str__(self):
		return self.client_company_name


# # Model: Portfolio
# class Portfolio(models.Model):
# 	portfolio_name = models.CharField(max_length=150)
# 	_image_full = models.ImageField(upload_to='gallery/%Y/%m/%d/', blank=False)
# 	_thumbnail = models.ImageField(upload_to='gallery/%Y/%m/%d/', blank=False)
# 	_image_title = models.CharField(max_length=200) 
# 	_image_description = models.CharField(max_length=200) 
# 	created = models.DateTimeField(auto_now_add=True)
# 	