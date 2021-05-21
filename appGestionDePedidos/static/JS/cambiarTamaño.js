function aumentar(){
    if (tamaño<30){
        tamaño += 5;
        texto.style.fontSize = `${tamaño}px`;
    } else {
        alert('Ya no se puede aumentar más!');
    }
}

function disminuir(){
    if (tamaño>10){
        tamaño -= 5;
        texto.style.fontSize = `${tamaño}px`;
    } else {
        alert('Ya no se puede disminuir más!');
    }
    
}

let texto = document.getElementById("texto");
let tamaño = parseFloat(getComputedStyle(texto).getPropertyValue('font-size'));

let botonAumentar = document.getElementById("aumentarTamaño");
botonAumentar.addEventListener("click", aumentar);

let botonDisminuir = document.getElementById("disminuirTamaño");
botonDisminuir.addEventListener("click", disminuir);