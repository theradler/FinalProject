function setStarRanking(starValue) {
    var starPostion = starValue.id.slice(-1);
    for (var i = (parseInt(starPostion) + 1); i <= 5; i++) {
        var star = document.getElementById(('star' + i));
        star.setAttribute("class", "fa fa-star")
    }

    for (var i = starPostion; i > 0; i--) {
        var star = document.getElementById(('star' + i));
        star.setAttribute("class", "fa fa-star checked")
    }
    console.log(starPostion); 

}