
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from datetime import datetime
from app.moviedbAPIInterface import moviedbAPIInterface
from django.core import serializers
from django.contrib.auth import login as auth_login, authenticate, logout
import json
from app.forms import BootstrapAuthenticationForm, BootstrapRegistrationForm

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
    assert isinstance(request, HttpRequest)
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

def login(request):
    userCreationForm = BootstrapRegistrationForm
    loginForm = BootstrapAuthenticationForm
    return render(
        request,
        'app/login.html',
        {
            'loginForm': loginForm,
            'regForm': userCreationForm,
        }
     )

def register(request):
    if request.method == 'POST':
        userCreationForm = BootstrapRegistrationForm(request.POST)
        if(userCreationForm.is_valid()):
            userCreationForm.save()
            username = userCreationForm.cleaned_data.get('username')
            raw_password = userCreationForm.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return HttpResponseRedirect('/moviesearch')
        else:
            loginForm = BootstrapAuthenticationForm()
            return render(
                 request,
                 'app/login.html',
                 {
                 'loginForm': loginForm,
                 'regForm': userCreationForm,
                }
                        )
      

def userAuth(request):
    if request.method == 'POST':
        loginForm = BootstrapAuthenticationForm(data=request.POST)
        if(loginForm.is_valid()):
            username = loginForm.cleaned_data.get('username')
            raw_password = loginForm.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return HttpResponseRedirect('/moviesearch')
        else:
            regForm = BootstrapRegistrationForm()
            return render(
                 request,
                 'app/login.html',
                 {
                 'loginForm': loginForm,
                 'regForm': userCreationForm,
                }
                        )