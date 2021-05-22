function insertarInfo(){
    var div = document.getElementById("saberMas");

    if(botonMasInfo.textContent == "Más sobre la herramienta"){
        div.insertAdjacentHTML('beforeend', texto);
        botonMasInfo.textContent = "Ocultar";
    } else {
        var textoMasInfo = document.getElementById("textoMasInfo");
        div.removeChild(textoMasInfo);
        botonMasInfo.textContent = "Más sobre la herramienta";
    }
    
}

let texto = `<div id="textoMasInfo">
<p>Esta herramienta permite:</p>
<ul>
    <li>Gestión completa de productos, pedidos, componentes, clientes</li>
    <li>Control de permisos según el cargo dentro de la empresa</li>
    <li>Interfaz sencilla para su manejo</li>
</ul>
</div>`

let botonMasInfo = document.getElementById("masInfo");
botonMasInfo.addEventListener("click", insertarInfo);