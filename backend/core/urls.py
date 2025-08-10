# core/urls.py

from django.urls import path
from . import views

# This 'app_name' helps Django differentiate URLs if you add more apps later.
app_name = 'core'

urlpatterns = [
    # URL for your homepage
    path('', views.homepage, name='homepage'),
    
    # URL for your "About Us" page
    path('about/', views.about_page, name='about'),

    # URL for your "Contact" page
    path('contact/', views.contact_page, name='contact'),

    # URL for your "Features" page
    path('features/', views.features_page, name='features'),

    # URL for your "Donate" page
    path('donate/', views.donate_page, name='donate'),
]