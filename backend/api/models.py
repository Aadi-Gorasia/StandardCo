# api/models.py

from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """ Represents a single user-created website project. """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    """ Represents a single page within a project (e.g., Home, About). """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='pages')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.project.name} - {self.name}"

class Section(models.Model):
    """ Represents a section on a page (e.g., Hero, Features). """
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='sections')
    section_type = models.CharField(max_length=50) # e.g., 'hero', 'feature_grid'
    order = models.PositiveIntegerField() # To maintain the order of sections on a page

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.page.name} - Section {self.order} ({self.section_type})"

class Component(models.Model):
    """ Represents a single piece of content within a section (e.g., a heading, a paragraph). """
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='components')
    component_type = models.CharField(max_length=50) # e.g., 'heading', 'paragraph', 'image'
    content = models.TextField() # The actual text or image URL
    
    def __str__(self):
        return f"{self.section} - {self.component_type}"