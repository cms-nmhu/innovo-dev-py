from django.contrib.auth.models import User

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView


class HomeView(TemplateView):
	template_name = 'home.html'

class AboutView(TemplateView):
	template_name = 'about.html'

class ContactView(TemplateView):
	template_name = 'contact.html'

class UserView(DetailView):
	model = User
	template_name = 'user.html'

	def get_context_data(self, **kwargs):
		context = super(UserView, self).get_context_data(**kwargs)
		context['prev_affiliations'] = self.get_object().innovouser.get_prev_affiliations_as_list()
		return context
