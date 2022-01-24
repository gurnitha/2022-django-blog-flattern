# apps/portfolio/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.portfolio.models import Slider, Service, Gallery, Client  

# Register your models here.


admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(Gallery)
admin.site.register(Client)