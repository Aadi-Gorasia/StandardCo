# accounts/views.py

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.

class SignUpView(CreateView):
    """
    This is a class-based view for handling user registration.
    
    It uses Django's built-in UserCreationForm to securely handle
    username, password, and password confirmation fields.
    """
    
    # The form that will be used to create a new user.
    form_class = UserCreationForm

    # Where to redirect the user after a successful sign-up.
    # 'reverse_lazy' is used here to prevent circular import issues.
    # It will redirect to the URL named 'login'. We will create this URL in the next steps.
    success_url = reverse_lazy('login')

    # The HTML template that will be used to display the sign-up form.
    # We will create this file next.
    template_name = 'accounts/signup.html'