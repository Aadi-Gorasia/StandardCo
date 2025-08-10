# accounts/urls.py - THE DEFINITIVE FIX

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # This file is now ONLY for our custom views.
    # The built-in login/logout views are now handled by the main urls.py.
    path('signup/', views.SignUpView.as_view(), name='signup'),
]