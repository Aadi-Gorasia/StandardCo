# api/models.py
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='pages')
    name = models.CharField(max_length=100, default='Home')

    def __str__(self):
        return f"{self.project.name} - {self.name}"

class Section(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='sections')
    section_type = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.page.name} - Section {self.order} ({self.section_type})"

class Component(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='components')
    component_type = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    styles = models.JSONField(default=dict) # To store things like color, font size, etc.
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.section} - Component ({self.component_type})"