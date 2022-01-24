# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # Portfolio
    path('', include('apps.portfolio.urls', namespace='portfolio')),

    # Admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:

    # Serve media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)