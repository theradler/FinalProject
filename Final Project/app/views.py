
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from app.moviedbAPIInterface import moviedbAPIInterface
from django.core import serializers
import json

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    search = moviedbAPIInterface()
    search.searchByTitle("titanic")
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def movieSearchPage(request):
    return render( 
        request,
        'app/moviesearch.html' )

def searchRequest(request, search_parameter,search_string):
    """On Page Search route"""
    print("recieved request")
    search = moviedbAPIInterface()
    if search_parameter == 'title':
        result = search.searchByTitle(search_string)
    elif search_parameter == 'person':
        result = search.searchByPerson(search_string)
    result = json.dumps(result)
    return HttpResponse(result) 
