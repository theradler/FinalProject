"""
Definition of urls for Final_Project.
"""

from datetime import datetime
from django.conf.urls import url
from django.urls import path
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    path('search/<str:search_parameter>/<str:search_string>', app.views.searchRequest, name='searchRequest'),
    url(r'^$', app.views.home, name='home'), 
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^moviesearch$',app.views.movieSearchPage, name='movieserchpage'),


     #Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     #Uncomment the next line to enable the admin:
     #url(r'^admin/', include(admin.site.urls)),
]
