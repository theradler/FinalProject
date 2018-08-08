function submitMovieSearch() {
    var searchParameters = getSearchParameters();
    var searchType = returnSearchBy(searchParameters.parameter);
    var url = '/search/' + searchType + '/' + searchParameters.query;
    var ajax = new XMLHttpRequest();
    ajax.onreadystatechange = function () {
        if (ajax.readyState == ajax.DONE && ajax.status == 200) {
            var returnObject = JSON.parse(ajax.responseText);
            renderSearchResults(returnObject);
        }
    };
    ajax.open("GET", url, true)
    ajax.send();
}


function renderSearchResults(searchResults) {
    results = searchResults;
    resultDisplayList = document.getElementById('resultsList');
    resultDisplayList.innerHTML = ''; 
    for (var i = 0; i < results.length; i++) {
        var li = document.createElement('li');
        li.className = 'media';
        li.appendChild(returnImageHTML(results[i].poster_path));
        li.appendChild(returnResultContentDiv(results[i]));
        li.appendChild(returnHorizontalRule());
        resultDisplayList.appendChild(li);
    }

}

function returnResultContentDiv(result) {
    var releaseDate = "Release Date: " + result.release_date;
    var overview;
    if (result.overview) {
        var overview = result.overview;
    } else {
        overview = "No description provided";
    }
    var contentDiv = document.createElement('div');
    contentDiv.setAttribute('class', 'media-body');
    contentDiv.appendChild(returnTitleHTML(result.original_title));
    contentDiv.appendChild(document.createTextNode(releaseDate));
    contentDiv.appendChild(returnLineBreak());
    contentDiv.appendChild(document.createTextNode(overview));
    contentDiv.appendChild(returnLineBreak());
    contentDiv.appendChild(returnAddToListButton(result));
    return contentDiv

}

function returnTitleHTML(titleText) {
    var title = document.createElement('h5');
    title.setAttribute('class', 'mt-0 mb-1');
    title.innerHTML = titleText;
    return title; 
}

function returnImageHTML(posterPath) {
    var img = document.createElement("img");
    img.className = "mr-3";
    img.width = "64";
    img.height = "104";
    if (posterPath) {
        img.src = "https://image.tmdb.org/t/p/original/" + posterPath;
    } else {
        img.src = "http://via.placeholder.com/" + img.width + "x" + img.height + "?text=No+Poster+Available"
    }
    img.alt = "poster for the movie"
    img.class = "poster "
    return img; 
}

function returnLineBreak() {
    var br = document.createElement('br');
    return br
}

function returnHorizontalRule() {
    var hr = document.createElement('span');
    hr.className = "border-top my-3"
    return hr 
}

function getSearchParameters() {
    var searchForm = document.getElementById('searchForm');
    var returnObject = {
        'parameter' : searchForm[0].value,
        'query' : searchForm[1].value
    }
    return returnObject
}

function returnSearchBy(parameter) {
    parameter = parameter.toLowerCase();
    switch (parameter) {
        case 'title':
            parameter = 'title';
            break;
        case 'person':
            parameter = 'person';
            break;
        case 'keyword':
            parameter = 'keyword';
            break;
        default:
            parameter = 'title'
    }
    return parameter;
}

function returnAddToListButton(result) {
    var button = document.createElement('button')
    button.className = "btn btn-primary btn-sm"
    button.type = "button"
    button.innerHTML = "Add to your Personal Canon"
    button.style.paddingTop = '10';
    button.style.paddingBottom = '10';
    button.style.margin = '10';
    button.value = result.id;
    button.setAttribute('onclick', 'onAddButtonClick(this.value)');
    return button
}

function onAddButtonClick(movieID) {
    var url = '/addMovie/' + movieID; 
    var ajax = new XMLHttpRequest();
    ajax.onreadystatechange = function () {
        if (ajax.readyState == ajax.DONE && ajax.status == 200) {
            if (ajax.responseText != 200) {
                document.getElementById('tooManyMovies').style.display = 'block';
            } else {
                window.location.href='/profile'
            }
        }
    };
    ajax.open("POST", url, true);
    ajax.setRequestHeader('X-CSRFToken', csrfToken);
    ajax.send();
}