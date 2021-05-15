function esperarResultadosIncorrectos(){

    let divi = document.getElementById('Busqueda');

    let producto = document.getElementsByClassName("Prueba");

    let aviso = document.createElement("div");

    aviso.innerHTML = (`<p>No se han encontrado resultados</p>`);

        if(!(producto.length>0))
        {
            divi.append(aviso);
        }
}

document.addEventListener("load", esperarResultadosIncorrectos())
