# api/urls.py

from django.urls import path
from . import views

# This 'app_name' helps Django differentiate URLs.
app_name = 'api'

urlpatterns = [
    # This URL is for listing all projects and creating a new one.
    # e.g., GET /api/projects/  OR  POST /api/projects/
    path('projects/', views.ProjectListCreateView.as_view(), name='project-list'),

    # This URL is for a single project's details.
    # The <int:pk> part is a variable that will hold the project's ID.
    # e.g., GET /api/projects/1/  OR  PUT /api/projects/1/
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
]