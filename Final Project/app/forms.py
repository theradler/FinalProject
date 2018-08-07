"""
Definition of forms.
"""

from django import forms
import django
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class BootstrapRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'palceholder':'User name'}))
    password1 = forms.CharField(label=("Password"),
                                widget=forms.PasswordInput({
                                    'class':'form-control',
                                    'placeholder':'Password'}))
    password2 = forms.CharField(label=("Password"),
                                widget=forms.PasswordInput({
                                    'class':'form-control',
                                    'placeholder':'Password'}))

class BoostrapCommentForm(forms.Form):
    comment = forms.CharField(label=("Comment"),
                              widget=forms.TextInput({
                                  'class':'pb-cmnt-textarea',
                                  'placeholder': 'Leave a Comment'
                                  }))
    listOwnerId = forms.IntegerField(widget=forms.HiddenInput())



class BoostrapMovieReview(forms.Form):
    reviewScore = forms.IntegerField(widget=forms.HiddenInput())

    reviewText = forms.CharField(label=("Leave a Review"),
                              widget=forms.TextInput({
                                  'class':'pb-cmnt-textarea',
                                  'placeholder': 'Enter Your Review'
                                  }))
