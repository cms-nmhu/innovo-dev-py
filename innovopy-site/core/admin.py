from django.contrib import admin

from .models import DocumentFile, InnovoUser, Category, InnovoTag, CpvCode

class InnovoUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'degree_type', 'degree', 'affiliation')
    list_editable = ['degree_type', 'degree']
    list_filter = ('degree_type', 'degree')


admin.site.register(DocumentFile)
admin.site.register(InnovoUser, InnovoUserAdmin)
admin.site.register(Category)
admin.site.register(InnovoTag)
admin.site.register(CpvCode)