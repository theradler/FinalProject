function renderList(movieList, isUserOwner) {
    var displaySection = document.getElementById('canonList')
    for (var i = 0; i < movieList.length; i++) {
        localMovie = movieList[i].fields
        var li = document.createElement('li');
        li.className = "media";
        li.id = localMovie.unique_id;
        li.appendChild(returnImageHTML(localMovie.poster_path));
        li.appendChild(returnContent(localMovie, isUserOwner));
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

function returnContent(movieObject, isUserOwner) {
    var details = movieObject.details
   
     
    details = JSON.parse(details);
    var releaseString = "Released: " + details.release_date;
    var runtimeString = "Runtime: " + details.runtime + " minutes";



    var masterDiv = document.createElement('div');
    masterDiv.className = "media-body";

    var title = document.createElement('h5');
    title.setAttribute('class', "mt-0 mb-1");
    title.innerHTML = movieObject.title;
    masterDiv.appendChild(title); 

    var subtitle = document.createElement('p');
    subtitle.innerHTML = "<strong><i>" + details.tagline + "</i></strong>";
    masterDiv.appendChild(subtitle);

    var releaseDate = document.createElement('p');
    releaseDate.innerHTML = releaseString
    masterDiv.appendChild(releaseDate);

    var runtime = document.createElement('p');
    runtime.innerHTML = runtimeString;
    masterDiv.appendChild(runtime);

    var overview = document.createElement('p');
    overview.innerHTML = details.overview;
    masterDiv.appendChild(overview);

    if (isUserOwner) {
        masterDiv.appendChild(returnRemoveFromListButton(movieObject.unique_id))
    }
    return masterDiv
}

function returnRemoveFromListButton(movieId) {
    var button = document.createElement('button')
    button.className = "btn btn-primary btn-sm"
    button.type = "button"
    button.innerHTML = "Remove from your Personal Canon"
    button.style.paddingTop = '10';
    button.style.paddingBottom = '10';
    button.style.margin = '10';
    button.value = movieId;
    button.setAttribute('onclick', 'onRemoveButtonClick(this.value)');
    return button
}


function onRemoveButtonClick(movieId) {
    console.log(movieId);
    var url = 'removeMovie/' + movieId;
    var ajax = new XMLHttpRequest();
    ajax.open("POST", url, true)
    ajax.setRequestHeader('X-CSRFToken', csrfToken);
    ajax.send(); 

    var removedItem = document.getElementById(movieId);
    removedItem.innerHTML = '';
}

function setListOwnerIdOnCommentForm(listOwnerID) {
    var hiddenField = document.getElementById('id_listOwnerId');
    hiddenField.value = listOwnerID
}
