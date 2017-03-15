from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Asset

custom_asset_property_list = (
	'title', 'building', 'room', 'short_desc', 'full_desc', 'contact_1_name', 'keywords',
	)

class AssetView(DetailView):
	model = Asset
	template_name = 'asset.html'

	def get_context_data(self, **kwargs):
		context = super(AssetView, self).get_context_data(**kwargs)
		context['asset_properties'] = self.get_object().get_as_dict_selected(custom_asset_property_list)
		return context


