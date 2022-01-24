# apps/portfolio/urls.py

# Django module
from django.urls import path

# Locals
from apps.portfolio.views import *

app_name = 'portfolio'

urlpatterns = [
    path('', index, name='homepage'),
    path('portfolio', portfolio, name='portfolio'),
]

