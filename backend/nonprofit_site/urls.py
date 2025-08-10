# nonprofit_site/urls.py

from django.contrib import admin
from django.urls import path, include
from builder import views as builder_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # This now correctly defines the one and only URL for our builder application.
    path('dashboard/', builder_views.dashboard, name='dashboard'),
    
    # This line is now deleted, as it's no longer needed.
    # path('dashboard/', include('builder.urls')), 

    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)