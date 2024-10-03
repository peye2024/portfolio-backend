from django.db import models
from django.utils.functional import cached_property
from coreapp.base import BaseModel


class Tag(BaseModel):
    title = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Project(BaseModel):
    title = models.CharField(max_length=100, unique=True)  # Title of the project
    excerpt = models.TextField(null=True, blank=True)  # Short description or summary
    slug = models.SlugField(max_length=100, unique=True, editable=False)  # URL slug
    description = models.TextField()  # Detailed project description
    thumbnail = models.ForeignKey('coreapp.Document', on_delete=models.CASCADE, related_name='project_thumbnail')
    images = models.ManyToManyField('coreapp.Document', related_name='project_images', blank=True)
    is_public = models.BooleanField(default=True)  # Whether the project is public or not
    tech_stack = models.TextField(null=True, blank=True)  # Technologies used, stored as a comma-separated list
    live_demo_url = models.URLField(null=True, blank=True)  # URL to live demo of the project
    github_url = models.URLField(null=True, blank=True)  # URL to GitHub repository
    completed_date = models.DateField(null=True, blank=True)  # Date when the project was completed

    def __str__(self):
        return self.title

    @cached_property
    def get_thumbnail_url(self):
        return self.thumbnail.get_url

    def save(self, *args, **kwargs):
        self.generate_slug('title')
        super(Project, self).save(**kwargs)
