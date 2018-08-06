
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from datetime import datetime
from app.moviedbAPIInterface import moviedbAPIInterface
from django.core import serializers
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.models import User
import json
from app.forms import BootstrapAuthenticationForm, BootstrapRegistrationForm, BoostrapCommentForm
from django.contrib.auth.decorators import login_required
from app.models import Movies, UserMovieList, Comments
from django.conf import settings
from django.utils.safestring import mark_safe

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    search = moviedbAPIInterface()
    search.searchByTitle("titanic")
    return render(request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })

def community(request):
    users = User.objects.exclude(pk=request.user.id)
    users = mark_safe(serializers.serialize('json',users))
    return render(request,
                  'app/community.html',
                  {
                      'communityUsers': users,
                  })

@login_required
def movieSearchPage(request):
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/moviesearch.html')

@login_required
def searchRequest(request, search_parameter,search_string):
    """On Page Search route"""
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
    return render(request,
        'app/login.html',
        {
            'loginForm': loginForm,
            'regForm': userCreationForm,
        })

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
            return render(request,
                 'app/login.html',
                 {
                 'loginForm': loginForm,
                 'regForm': userCreationForm,
                })
      

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
            return render(request,
                 'app/login.html',
                 {
                 'loginForm': loginForm,
                 'regForm': userCreationForm,
                })

@login_required
def addMovie(request, moviedb_id):
    if request.method == 'POST':
        current_user = request.user
        search = moviedbAPIInterface()
        result = search.getMovieById(moviedb_id)
        if not Movies.objects.filter(moviedb_id=moviedb_id).exists():
            newMovie = Movies(moviedb_id=moviedb_id,title=result['title'], poster_path=result['poster_path'], details=result['details'])
            newMovie.save()
        newListNumber = UserMovieList.objects.filter(user_id=current_user.id).count() + 1 
        currentMovie = Movies.objects.get(moviedb_id=moviedb_id)
        currentUser = User.objects.filter(pk=current_user.id) 
        newMovieListItem = UserMovieList(user=current_user,movie=currentMovie,list_position=newListNumber)
        newMovieListItem.save()
        return HttpResponse('Hello') 

@login_required
def removeMovieFromList(request, movieUnique_id):
    if request.method == 'POST':
        currentUserID = request.user.id; 
        movieToRemove = Movies.objects.get(unique_id=movieUnique_id)
        currentUser = User.objects.get(pk=currentUserID)
        UserMovieList.objects.filter(movie=movieToRemove).filter(user=currentUser).delete()
        return HttpResponse('200')

@login_required
def myProfile(request):
    currentUserID = request.user.id
    listData = UserMovieList.objects.filter(user_id=currentUserID)
    movieList = listData.values_list('movie', flat=True) 
    movieList = Movies.objects.filter(pk__in=movieList).order_by('usermovielist__list_position')
    movieList = mark_safe(serializers.serialize('json', movieList))
    return render(request,
        'app/userprofile.html',
        {'movieList':movieList, 
         'listOwner': request.user.username
         })

@login_required
def otherProfile(request,username):
    profileOwner = User.objects.get(username=username)
    commentForm = BoostrapCommentForm()
    listData = UserMovieList.objects.filter(user=profileOwner)
    movieList  = listData.values_list('movie',flat=True)
    movieList = Movies.objects.filter(pk__in=movieList).order_by('usermovielist__list_position')
    movieList = mark_safe(serializers.serialize('json', movieList))
    return render(request,
        'app/userprofile.html',
        {'movieList':movieList, 
         'listOwner': username,
         'commentForm':commentForm,
         'ownerID': profileOwner.pk
         })
@login_required
def submitComment(request):
    if request.method == 'POST':
        commentForm = BoostrapCommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.cleaned_data.get('comment')
            listOwnerId = commentForm.cleaned_data.get('listOwnerId')
            userList = User.objects.get(pk=listOwnerId)
            commentOwner = User.objects.get(pk=request.user.id).username
            newComment = Comments(userList=userList,commentOwner=commentOwner,comments=comment)
            newComment.save() 
            print('commentReceived')
    return HttpResponse('shit worked')
