import requests
import json


class moviedbAPIInterface(object):
    """Retruns List of Movies based on 3 different search parameters"""

    def __init__(self, *args, **kwargs):
        self.api_key = 'c12e04ddf08a6d3eb80ab6342221346f'
        self.language = 'en-US'
        self.include_adult = 'false' 
            
        return super().__init__(*args, **kwargs)

    def searchByTitle(self,query):
        query = query.replace(" ", "%20")
        url = 'https://api.themoviedb.org/3/search/movie?api_key=' + self.api_key + '&language=' + self.language + "&query=" + query + "&include_adult=" + self.include_adult
        response = requests.get(url)
        returnBody = json.loads(response.text)
        returnBody = returnBody['results']
        return returnBody

    def searchByPerson(self,query):
        query = query.replace(" ", "%20")
        movieList = []
        url = 'https://api.themoviedb.org/3/search/person?api_key=' + self.api_key + '&language=' + self.language + "&query=" + query + "&include_adult=" + self.include_adult
        response = requests.get(url)
        returnBody = json.loads(response.text)
        returnBody = returnBody['results']
        i = 0
        while i < len(returnBody):
            knownFor = returnBody[i]['known_for']
            newList = [ item for item in knownFor if item['media_type'] == 'movie']
            movieList = movieList + newList
            i += 1
        response =  movieList
        return response

    def getMovieById(self, movieID):
        url='https://api.themoviedb.org/3/movie/' + movieID + '?api_key=' + self.api_key + '&language=' + self.language
        response = requests.get(url)
        response = json.loads(response.text)
        overview = response['overview']
        details = {'overview': response['overview'],
                   'genres': response['genres'],
                   'release_date': response['release_date'],
                   'runtime': response['runtime'],
                   'tagline': response['tagline']
                   }
        movieObject = {'details':details,
                       'title': response['title'],
                       'moviedb_id': movieID,
                       'poster_path': response['poster_path']
                       }
        return movieObject
    

