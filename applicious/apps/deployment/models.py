from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django_extensions.models import TimeStampedModel, TitleSlugDescriptionModel


class Repositories(TimeStampedModel, TitleSlugDescriptionModel):
    """
    Main Post Content
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.Charfield(max_length=100, unique=True)
    category = models.OneToOneField('Categories', Blank=True)
    summary = models.CharField(max_length=255)

    ssh_url = models.CharField(max_length=255)
    https_url = models.CharField(max_length=255)

    rules = models.TextField()
    last_push = models.DateTimeField(null=True)
    last_push = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Repositories'

    def __unicode__(self):
        return self.title


class Categories(TimeStampedModel, TitleSlugDescriptionModel):
    """
    Optional Categories for Posts
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.Charfield(max_length=100, unique=True)
    summary = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-title']
        verbose_name_plural = 'Categories'
