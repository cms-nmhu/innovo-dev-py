from __future__ import unicode_literals

from django.db import models
from core.models import DocumentFile

ORG_TYPES = (
    (0, 'college'),
    (1, 'department'),
    (2, 'lab'),
    (3, 'research group'),
    (4, 'division'),
    (5, 'other')
)

class Innovosite(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)

    documents = models.ManyToManyField(DocumentFile, related_name='site_documents', blank=True)

    def get_absolute_url(self):
        return reverse('innovosite', args=[self.id])

    def __unicode__(self):
        return self.name

""" The following two functions need to be refactored. Do not use.
    def get_org_tree(self, orgstack, org, level):
        print level, org, org.childorgs.all()
        d = {}
        for i in org.childorgs.all():
            try:
                o = orgstack.pop(i.id)
                d[o] = o.get_org_tree(orgstack, o, level+'-')
            except Exception as e:
                print e
                pass
        return d

    def get_children(self):
        orgs = self.suborganizations.all().order_by('org_type', 'name')
        orgstack = {i.id : i for i in orgs}
        subs = []
        for i in orgs:
            try:
                o = orgstack.pop(i.id)
                d = {o: self.get_org_tree(orgstack, o, '-')}
                subs.append(d)
            except:
                pass
        return subs
"""




class SubOrganization(models.Model):
    name = models.CharField(max_length=256)
    org_type = models.IntegerField(choices=ORG_TYPES, default=5)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    org_site = models.ForeignKey(Innovosite, related_name = 'suborganizations')
    org_parent = models.ForeignKey('SubOrganization', null=True, blank=True, related_name = 'childorgs')

    documents = models.ManyToManyField(DocumentFile, related_name='organization_documents', blank=True)

    def get_children(self):
        chnodes = list(self.childorgs.all())
        for i in chnodes:
            chnodes += i.get_children()

        return chnodes

    def get_absolute_url(self):
        return reverse('unit', args=[self.id])

    def __unicode__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=48, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    building_site = models.ForeignKey(Innovosite)

    documents = models.ManyToManyField(DocumentFile, related_name='building_documents', blank=True)
    
    def get_absolute_url(self):
        return reverse('building', args=[self.id])

    def __unicode__(self):
        return self.name























