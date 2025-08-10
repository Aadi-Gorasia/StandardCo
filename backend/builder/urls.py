# builder/urls.py

from django.urls import path
from . import views

app_name = 'builder'

# This list is now empty because all builder-related URLs (like the main dashboard)
# are now handled in the main nonprofit_site/urls.py file.
# We are keeping this file for now in case we add more complex builder URLs later.
urlpatterns = [
    # path('create/portfolio/', views.create_portfolio_view, name='create_portfolio'), # This line is deleted
]