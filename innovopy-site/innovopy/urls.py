"""innovopy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from haystack.forms import FacetedSearchForm
from haystack.generic_views import FacetedSearchView

# import debug_toolbar

from core.views import HomeView, AboutView, ContactView, UserView
from innovosite.views import InnovositeView, InnovositeListView
from innovosite.views import SubOrganizationView, SubOrganizationListView, BuildingView
from asset.views import AssetView

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^search/', include('haystack.urls')),
    url(r'^search/', FacetedSearchView.as_view(form_class=FacetedSearchForm, facet_fields=['room', 'contact_1_name', 'manufacturer' ]), name='haystack_search'),
	url(r'^about/$', AboutView.as_view(), name='about'),
	url(r'^contact/$', ContactView.as_view(), name='contact'),
    
    url(r'^innovo-sites/$', InnovositeListView.as_view(), name='innovosite_list'),
    url(r'^innovo/(?P<pk>[0-9]+)/$', InnovositeView.as_view(), name='innovosite'),
    
    url(r'^units/$', SubOrganizationListView.as_view(), name='unit_list'),
    url(r'^unit/(?P<pk>[0-9]+)/$', SubOrganizationView.as_view(), name='unit'),
    
    url(r'^building/(?P<pk>[0-9]+)/$', BuildingView.as_view(), name='building'),
    url(r'^asset/(?P<pk>[0-9]+)/$', AssetView.as_view(), name='asset'),
    
    url(r'^user/(?P<pk>[0-9]+)/$', UserView.as_view(), name='user_view'),
    
    url(r'^admin/', admin.site.urls),

    # url(r'^__debug__/', include(debug_toolbar.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    # url(r'^$', FacetedSearchView(form_class=FacetedSearchForm, facet_fields=['author']), name='haystack_search'),

    # url(r'^search/', FacetedSearchView.as_view(form_class=FacetedSearchForm, facet_fields=['room'],template_name='search/search.html', context_object_name='page_object'), name='haystack_search'),
