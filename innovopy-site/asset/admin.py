from django.contrib import admin

from .models import Asset, AssetCategory


class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model_name', 'organization', 'building')
    list_filter = ('organization', 'building', 'contact_1_name')

class AssetCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'asset', 'category')
    list_filter = ('asset', 'category')


admin.site.register(Asset, AssetAdmin)
admin.site.register(AssetCategory, AssetCategoryAdmin)
