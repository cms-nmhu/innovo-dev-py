from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import Innovosite, SubOrganization, Building

class InnovositeView(DetailView):
	model = Innovosite
	template_name = 'innovosite.html'


	def get_nodes(self, orgstack, org, level):
	    d = {}
	    for i in org.childorgs.all():
	        try:
	            o = orgstack.pop(i.id)
	            d[o] = self.get_nodes(orgstack, o, level+'-')
	        except:
	            pass
	    return d

	def get_context_data(self, **kwargs):
		context = super(InnovositeView, self).get_context_data(**kwargs)

		orgs = self.get_object().suborganizations.all().order_by('org_type', 'name')
		orgstack = {i.id : i for i in orgs}
		subs = []
		for i in orgs:
		    try:
		        o = orgstack.pop(i.id)
		        d = {o: self.get_nodes(orgstack, o, '-')}
		        subs.append(d)
		    except:
		        pass

		# print s

		# for n in subs:
		#     print_node(n, '-')



		context['suborgs'] = subs #self.get_object().suborganizations.all()
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
