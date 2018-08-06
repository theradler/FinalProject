
from django.contrib import admin

from app.models import Movies, UserMovieList, Comments

admin.site.register(Movies)
admin.site.register(UserMovieList)
admin.site.register(Comments)