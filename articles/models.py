from coreapp.base import BaseModel
from django.db import models
from django.utils.functional import cached_property

from project.models import Tag


class Article(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    description = models.TextField()
    thumbnail = models.ForeignKey('coreapp.Document', on_delete=models.CASCADE, related_name='article_thumbnail')
    images = models.ManyToManyField('coreapp.Document', related_name='article_images', blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @cached_property
    def get_thumbnail_url(self):
        return self.thumbnail.get_url

    def save(self, *args, **kwargs):
        self.generate_slug('title')
        super(Article, self).save(**kwargs)
