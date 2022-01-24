# apps/portfolio/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.portfolio.models import Slider, Service  

# Register your models here.


admin.site.register(Slider)
admin.site.register(Service)