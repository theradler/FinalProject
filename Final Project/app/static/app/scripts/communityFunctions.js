function renderUsers(communityUsers) {
    for (var i = 0; i < communityUsers.length; i++) {
        localModel = communityUsers[i].fields
        renderListLink(localModel.username);
    }
}


function renderListLink(username) {
    var listMaster = document.getElementById('usersList');
    var a = document.createElement('a');
    a.className = "list-group-item list-group-item-action"
    a.innerHTML = username
    a.href = "/profile/" + username;
    listMaster.appendChild(a);

}