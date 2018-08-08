//Controls star review and sets hidden field in form 
function setStarRanking(starValue) {
    var starPostion = starValue.id.slice(-1);
    for (var i = (parseInt(starPostion) + 1); i <= 5; i++) {
        var star = document.getElementById(('star' + i));
        star.setAttribute("class", "fa fa-star")
    }

    for (var i = starPostion; i > 0; i--) {
        var star = document.getElementById(('star' + i));
        star.setAttribute("class", "fa fa-star checked");
    }

    var formField = document.getElementById('id_reviewScore');
    formField.value = starPostion;
    var submitButton = document.getElementById('commentSubmitButton');
    submitButton.disabled = false;
    submitButton.title = "";

}