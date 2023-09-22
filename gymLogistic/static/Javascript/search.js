function fetchResults(){
    var query = documents.getElementById('search').value;
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/search/?q=' + query, true);
    xhr.onload = function() {
        if (this.status == 200){
        document.getElementById('results').innerHTML = this.responseText;
        }
    };
    xhr.send()
}


