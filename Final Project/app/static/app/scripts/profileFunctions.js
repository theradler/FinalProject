function renderList(movieList, ) {
    var displaySection = document.getElementById('canonList')
    for (var i = 0; i < movieList.length; i++) {
        localMovie = movieList[i].fields
        var li = document.createElement('li');
        li.className = "media"; 
        li.appendChild(returnImageHTML(localMovie.poster_path));
        li.appendChild(returnContent(localMovie));
        displaySection.appendChild(li);
    }
}

function returnImageHTML(posterPath) {
    var img = document.createElement("img");
    img.className = "mr-3";
    img.width = "200";
    if (posterPath) {
        img.src = "https://image.tmdb.org/t/p/original/" + posterPath;
    } else {
        img.src = "http://via.placeholder.com/" + img.width + "x" + img.height + "?text=No+Poster+Available"
    }
    img.alt = "poster for the movie"
    img.class = "poster "
    return img;
}

function returnContent(movieObject) {
    console.log(movieObject)
    var details = movieObject.details
    details = JSON.parse(details);
    var masterDiv = document.createElement('div');
    masterDiv.className = "media-body";

    var title = document.createElement('h5');
    title.setAttribute('class', "mt-0 mb-1");
    title.innerHTML = movieObject.title;
    masterDiv.appendChild(title); 

    var subtitle = document.createElement('blockquote');
    subtitle.innerHTML = movieObject.details.tagline;
    masterDiv.appendChild(subtitle);




    return masterDiv
}

