from django.contrib import admin

from .models import Innovosite, SubOrganization, Building

class InnovositeAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

class SubOrganizationAdmin(admin.ModelAdmin):
    list_editable = ('org_site', 'org_type', 'org_parent')
    list_display = ('name', 'org_site', 'org_type', 'org_parent')
    list_filter = ('org_site', 'org_type', 'org_parent')

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'building_site')
    list_filter = ('building_site',)

admin.site.register(Innovosite, InnovositeAdmin)
admin.site.register(SubOrganization, SubOrganizationAdmin)
admin.site.register(Building, BuildingAdmin)
