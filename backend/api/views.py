# api/views.py

from rest_framework import generics, permissions
from .models import Project
from .serializers import ProjectSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    """
    This view handles listing and creating projects for the logged-in user.
    - A GET request will list all projects owned by the current user.
    - A POST request will create a new project owned by the current user.
    """
    serializer_class = ProjectSerializer
    
    # This is the crucial security part. It ensures that users can only
    # interact with their own projects and must be logged in to do so.
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This method is overridden to filter the projects and return only
        the ones that belong to the currently logged-in user.
        """
        return Project.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        This method is called when a new project is created (via a POST request).
        It automatically assigns the currently logged-in user as the project's owner.
        """
        serializer.save(user=self.request.user)