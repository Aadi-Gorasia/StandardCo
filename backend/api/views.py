# api/views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Project, Page, Section, Component
from .serializers import ProjectListSerializer, ProjectDetailSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    """
    Handles listing basic project info and creating new, empty projects.
    """
    serializer_class = ProjectListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # When a new project is created, also create a default "Home" page for it.
        project = serializer.save(user=self.request.user)
        Page.objects.create(project=project, name='Home')


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single, detailed project.
    """
    serializer_class = ProjectDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        """
        This is a custom update method to handle our complex nested data.
        This is the core of the "Save" functionality.
        """
        project = self.get_object()
        data = request.data
        
        # Update the project's name
        project.name = data.get('name', project.name)
        project.save()

        # We expect the frontend to send page data in a 'pages' list
        pages_data = data.get('pages', [])
        for page_data in pages_data:
            page, _ = Page.objects.get_or_create(id=page_data.get('id'), project=project)
            
            # Clear existing sections and components to rebuild them
            page.sections.all().delete()
            
            sections_data = page_data.get('sections', [])
            for section_data in sections_data:
                section = Section.objects.create(
                    page=page,
                    section_type=section_data.get('section_type'),
                    order=section_data.get('order')
                )
                
                components_data = section_data.get('components', [])
                for component_data in components_data:
                    Component.objects.create(
                        section=section,
                        component_type=component_data.get('component_type'),
                        content=component_data.get('content', ''),
                        styles=component_data.get('styles', {}),
                        order=component_data.get('order')
                    )

        # Return the updated, full project structure
        serializer = self.get_serializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)