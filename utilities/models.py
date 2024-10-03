from coreapp.base import BaseModel
from django.db import models


class ContactMessage(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} -- {self.email}'


class Maintainer(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ForeignKey('coreapp.Document', on_delete=models.CASCADE)
    introduction = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    github_url = models.URLField()
    linkedin_url = models.URLField()
    facebook_url = models.URLField()

    def __str__(self):
        return f'{self.name}'
