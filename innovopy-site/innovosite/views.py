from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import Innovosite, SubOrganization, Building

class InnovositeView(DetailView):
	model = Innovosite
	template_name = 'innovosite.html'

	def get_context_data(self, **kwargs):
		context = super(InnovositeView, self).get_context_data(**kwargs)
		context['suborgs'] = self.get_object().suborganizations.all()
		return context


class InnovositeListView(ListView):
	model = Innovosite
	template_name = 'innovosite_list.html'


class SubOrganizationView(DetailView):
	model = SubOrganization
	template_name = 'suborg.html'

	def get_context_data(self, **kwargs):
		context = super(SubOrganizationView, self).get_context_data(**kwargs)
		assets = self.get_object().assets.all()
		manufacturers = {}
		for i in assets:
			manufacturers[i.manufacturer] = i.manufacturer_website
		context['manufacturers'] = manufacturers
		context['assets'] = assets
		return context


class SubOrganizationListView(ListView):
	model = SubOrganization
	template_name = 'suborg_list.html'



class BuildingView(DetailView):
	model = Building
	template_name = 'building.html'
