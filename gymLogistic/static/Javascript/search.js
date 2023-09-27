document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();
    var busqueda = document.querySelector('input[name="busqueda"]').value.toLowerCase();
    document.querySelectorAll('.objeto').forEach(function(objeto) {
        var nombre = objeto.querySelector('p').textContent.toLowerCase();
        if(nombre.includes(busqueda)) {
            objeto.styles.display = '';
        } else {
            objeto.styles.display = 'none';
        }
    });
});



