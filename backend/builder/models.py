# builder/models.py

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GeneratedProject(models.Model):
    """
    This model represents a single website that a user has generated.
    Each time a user clicks "Generate & Download", a new entry will be
    created in this database table.
    """

    # A link to the user who created this project.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # The name of the template they used, e.g., "portfolio".
    template_name = models.CharField(max_length=100)

    # NEW: An image field to store the user's uploaded profile picture.
    # The 'upload_to' parameter tells Django to save these images in a 'uploads/'
    # directory inside our media root.
    profile_picture = models.ImageField(upload_to='uploads/', null=True, blank=True)

    # A timestamp that is automatically set the moment this project is created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # This provides a nice, human-readable name for each project in the Django admin.
        return f"{self.user.username}'s {self.template_name} project on {self.created_at.strftime('%Y-%m-%d')}"