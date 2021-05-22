/*Funcion que llama el EventListener. Primero se localiza el boton creado en "base.html" y se comprueba el texto del boton. Dependiendo del estado oculta o muestra la variable texto*/
function insertarInfo(){
    var div = document.getElementById("saberMas");

    /*Si se ejecuta el if, el texto esta oculto y por ello se cambia el nombre del boton y se muestra el texto*/
    if(botonMasInfo.textContent == "Más sobre la herramienta"){
        div.insertAdjacentHTML('beforeend', texto);
        botonMasInfo.textContent = "Ocultar";
        /*Si se ejecuta el else, es que el texto esta visible, y se oculta a la vez que se cambia el nombre al boton de nuevo */
    } else {
        var textoMasInfo = document.getElementById("textoMasInfo");
        div.removeChild(textoMasInfo);
        botonMasInfo.textContent = "Más sobre la herramienta";
    }
    
}

/*Variable que guarda el texto que se muestra al hacer click en mas informacion */
let texto = `<div id="textoMasInfo">
<p>Esta herramienta permite:</p>
<ul>
    <li>Gestión completa de productos, pedidos, componentes, clientes</li>
    <li>Control de permisos según el cargo dentro de la empresa</li>
    <li>Interfaz sencilla para su manejo</li>
</ul>
</div>`

/*Variable que encuentra el boton y añade un EventListener, llamando a la funcion "insertarInfo"*/
let botonMasInfo = document.getElementById("masInfo");
botonMasInfo.addEventListener("click", insertarInfo);