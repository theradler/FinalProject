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
from django.contrib.auth.views import logout
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    path('search/<str:search_parameter>/<str:search_string>', app.views.searchRequest, name='searchRequest'),
    path('movie/<str:movieUniqueId>',app.views.movieProfile, name='movieProfile' ),
    path('addMovie/<str:moviedb_id>',app.views.addMovie, name='addMovie'),
    path('removeMovie/<str:movieUnique_id>', app.views.removeMovieFromList, name='removeMovie'),
    path('profile/<str:username>', app.views.otherProfile, name='otherProfile'),
    path('submitReview/<str:movieUniqueId>', app.views.submitReview, name='submitReview'),
    url(r'^$', app.views.home, name='home'), 
    url(r'^login/$',app.views.login, name='login'),
    url(r'^logout$',
        logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^moviesearch$',app.views.movieSearchPage, name='movieserchpage'),
    url(r'^register$', app.views.register, name='register'), 
    url(r'^userAuth$', app.views.userAuth, name='userauth'),
    url(r'^profile$', app.views.myProfile, name='myProfile'),
    url(r'^community$', app.views.community, name='community'),
    url(r'^submitComment',app.views.submitComment, name='submitComment'),


     #Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     #Uncomment the next line to enable the admin:
     url(r'^admin/', admin.site.urls),
]
