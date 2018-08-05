"""
Definition of urls for Final_Project.
"""

from datetime import datetime
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
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
    url(r'^login/$',app.views.login, name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^moviesearch$',app.views.movieSearchPage, name='movieserchpage'),
    url(r'^register$', app.views.register, name='register'), 
    url(r'^userAuth$', app.views.userAuth, name='userauth'),


     #Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     #Uncomment the next line to enable the admin:
     url(r'^admin/', admin.site.urls),
]
