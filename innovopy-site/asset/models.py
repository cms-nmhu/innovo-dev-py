from __future__ import unicode_literals

from collections import OrderedDict

from django.db import models

from innovosite.models import Innovosite, SubOrganization, Building 
from core.models import DocumentFile 

AVAILABILITY = (
    ('available', 'available'),
    ('under maintenance', 'under maintenance'),
    ('in-use', 'currently in use'),
    ('under repair', 'currently under repair'),
    ('not operational', 'not operational')
)

class Asset(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    organization = models.ForeignKey(SubOrganization, null=True, related_name="assets", blank=True)
    building =  models.ForeignKey(Building, null=True, blank=True)
    room = models.CharField(max_length=256, null=True, blank=True)
    model_name = models.CharField(max_length=256, null=True, blank=True)
    manufacturer = models.CharField(max_length=256, null=True, blank=True)
    manufacturer_website = models.CharField(max_length=256, null=True, blank=True)
    year_of_manufacture = models.IntegerField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    short_desc = models.CharField(max_length=256, null=True, blank=True)
    full_desc = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    related_media = models.ManyToManyField(DocumentFile, blank=True)

    contact_1_name = models.CharField(max_length=256, null=True, blank=True)
    contact_1_email = models.CharField(max_length=256, null=True, blank=True)
    contact_2_name = models.CharField(max_length=256, null=True, blank=True)
    contact_2_email = models.CharField(max_length=256, null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_of_purchase = models.DateTimeField(null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    asset_no = models.CharField(max_length=256, null=True, blank=True)
    availability = models.CharField(max_length=256, choices=AVAILABILITY, null=True, default='available')
    cost = models.CharField(max_length=256, null=True, blank=True) 
    quantity = models.IntegerField(default=1)
    serial_no = models.CharField(max_length=256, null=True, blank=True)
    specification = models.TextField(null=True, blank=True)

    def get_as_dict_selected(self, fieldlist=None):
        d = OrderedDict()
        if not fieldlist:
            fieldlist = ('title', 'building', 'room', 'short_desc', 'full_desc', 'contact_1_name', 'contact_1_email',)
        for field in fieldlist:
            prop = eval('self.'+field)
            d[field] = prop or ''
        return d            

    def get_as_dict(self):
        d = {}
        for field in [ f.name for f in self._meta.get_fields(include_parents=False)]:
            prop = eval('self.'+field)
            d[field] = prop or ''
        return d

    def get_specification_as_list(self):
        items = self.specification.split('*')
        return items

    def get_absolute_url(self):
        return reverse('asset', args=[self.id])

    def __unicode__(self):
        return self.title or 'no title here'





""" TODO: Modeling associations"""

#  item -> tag
#  item -> category
#  item -> publications
#  item -> users
#  item -> files

