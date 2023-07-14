(function(){
    var actualizarHora = function() {
        var fecha = new Date(),
            horas = fecha.getHours(),
            minutos = fecha.getMinutes(),
            dia = fecha.getDate(),
            mes = fecha.getMonth() + 1,
            año = fecha.getFullYear();
        
        var pHoras = document.getElementById('horas'),
            pMinutos = document.getElementById('minutos'),
            pFecha = document.getElementById('fecha');

        if (horas < 10) {
            horas = "0" + horas;
        }

        if (minutos < 10) {
            minutos = "0" + minutos;
        }

        pHoras.textContent = horas;
        pMinutos.textContent = minutos;

        pFecha.textContent = dia + '/' + mes + '/' + año;
    }

    actualizarHora();
    var intervalo = setInterval(actualizarHora, 1000);
})();


