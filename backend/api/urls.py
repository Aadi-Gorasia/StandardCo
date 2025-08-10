# api/urls.py

from django.urls import path
from . import views

# This 'app_name' helps Django differentiate URLs.
app_name = 'api'

urlpatterns = [
    # This creates the URL pattern for our project list endpoint.
    # The final URL will be "/api/projects/".
    # It points to the ProjectListCreateView we just made.
    # .as_view() is required for class-based views.
    path('projects/', views.ProjectListCreateView.as_view(), name='project-list'),
]