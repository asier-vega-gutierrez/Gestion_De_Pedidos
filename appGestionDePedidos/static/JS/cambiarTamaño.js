/*Funcion que llama el EventListener si el usuario hace click en el boton de aumentar tamaño. Se coge el tamaño actual del texto y lo aumenta en 5px*/
function aumentar(){
    /*Si el tamaño del texto es menor que 30px, lo aumenta 5px más*/
    if (tamaño<30){
        tamaño += 5;
        texto.style.fontSize = `${tamaño}px`;
    /*Si el tamaño del texto es mayor o igual que 30px, saldrá un aviso de que no se puede aumentar más el tamaño*/
    } else {
        alert('Ya no se puede aumentar más!');
    }
}

/*Funcion que llama el EventListener si el usuario hace click en el boton de disminuir tamaño. Se coge el tamaño actual del texto y lo reduce en 5px*/
function disminuir(){
    /*Si el tamaño del texto es mayor que 10px, lo reduce 5px más*/
    if (tamaño>10){
        tamaño -= 5;
        texto.style.fontSize = `${tamaño}px`;
    /*Si el tamaño del texto es menor o igual que 10px, saldrá un aviso de que no se puede reducir más el tamaño*/
    } else {
        alert('Ya no se puede disminuir más!');
    }
    
}

/*Variables donde se guardan el texto a aumentar/disminuir (texto) y el tamaño actual de dicho texto (tamaño)*/
let texto = document.getElementById("texto");
let tamaño = parseFloat(getComputedStyle(texto).getPropertyValue('font-size'));

/*Variable donde se guarda el boton de aumentar y añade un EventListener, llamando a la funcion "aumentar"*/
let botonAumentar = document.getElementById("aumentarTamaño");
botonAumentar.addEventListener("click", aumentar);

/*Variable donde se guarda el boton de disminuir y añade un EventListener, llamando a la funcion "disminuir"*/
let botonDisminuir = document.getElementById("disminuirTamaño");
botonDisminuir.addEventListener("click", disminuir);