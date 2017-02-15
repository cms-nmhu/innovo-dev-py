from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

DEGREE_TYPES = (
    (0, 'No Degree'),
    (1, 'Associates'),
    (2, 'Bachelors'),
    (3, 'Masters'),
    (4, 'Doctorate'),
)

class DocumentFile(models.Model):
    file = models.FileField(null=True)

    def __unicode__(self):
        return self.file.name

class InnovoUser(models.Model):
    user = models.OneToOneField(User)
    degree_type = models.IntegerField(choices=DEGREE_TYPES, blank=True, default=0)
    degree = models.CharField(max_length=512, blank=True, null=True)
    affiliation = models.CharField(max_length=512, blank=True, null=True)
    prev_affiliations = models.TextField(blank=True, null=True)
    prev_positions = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username


class Publication(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(null=True)
    bibtex = models.TextField(null=True)
    file = models.FileField(null=True)
    
    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class InnovoTag(models.Model):
    tag = models.CharField(max_length=255)

    def __unicode__(self):
        return self.tag


class CpvCode(models.Model):
    cpv_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name




