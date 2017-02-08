from django.shortcuts import render
from django.views.generic import TemplateView, DetailView


class HomeView(TemplateView):
	template_name = 'home.html'

class AboutView(TemplateView):
	template_name = 'about.html'

class ContactView(TemplateView):
	template_name = 'contact.html'

class UserView(DetailView):
	template_name = 'user.html'


