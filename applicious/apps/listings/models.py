from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django_extensions.models import TimeStampedModel, TitleSlugDescriptionModel


class Listings(TimeStampedModel, TitleSlugDescriptionModel):
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=255)
    body = models.TextField()
    status = models.CharField(choices=(
        ('draft', 'Draft',)
        ('published', 'Published')
    ))
    published_on = models.DateTimeField(null=True)
    is_featured = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Listings'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.summary:
            self.summary = make_summary(self.content.raw)
        if self.status == 'published':
            self.published_on = datetime.now()

        super(Listings, self).save(*args, **kwargs)

