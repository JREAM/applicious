from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django_extensions.models import TimeStampedModel, TitleSlugDescriptionModel


class Posts(TimeStampedModel, TitleSlugDescriptionModel):
    """
    Main Post Content
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.Charfield(max_length=100, unique=True)
    category = models.OneToOneField('Categories', Blank=True)
    summary = models.CharField(max_length=255)
    body = models.TextField()
    status = models.CharField(choices=(
        ('draft', 'Draft',)
        ('published', 'Published')
    ))
    published_on = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Posts'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.summary:
            self.summary = make_summary(self.body.raw)
        if self.status == 'published':
            self.published_on = datetime.now()

        super(Posts, self).save(*args, **kwargs)


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


class Tags(TimeStampedModel, TitleSlugDescriptionModel):
    """
    Optional Tags for Posts
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30, unique=True)
    post = models.ForeignKey(Posts)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-title']
        verbose_name_plural = 'Tags'


class Comments(TimeStampedModel):
    """
    Comments for Posts
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default='anonymous')
    title = models.CharField(max_length=100)
    body = models.TextField()
    post = models.ForeignKey(Posts)
    status = models.CharField(choices=(
        ('public', 'Public')
        ('spam', 'Spam'),
    ), default='public')

    user_ip = models.IPAddressField(null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Comments'


def make_summary(summary):
    """
    Creates a Summary if one does not exist
    """
    return ' '.join(summary.split()[:125])
