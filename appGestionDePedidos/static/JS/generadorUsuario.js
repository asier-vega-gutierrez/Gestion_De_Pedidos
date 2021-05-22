/*esta funcion coje el nombre + apellido introducido les añade un nuemero aleatorio y muestra el resultado en el usuario */
function generarUsuario(event){

    let usuarioGenericoParte1 = campoNombre.childNodes[1].childNodes[3].value
    let usuarioGenericoParte2 = campoApellido.childNodes[1].childNodes[3].value
    let usuarioGenericoParte3 = Math.floor(Math.random() * 10)

    let usuarioFinal = usuarioGenericoParte1 +  usuarioGenericoParte2 + String(usuarioGenericoParte3)
    usuarioFinal = ponerPrimeraMayuscula(usuarioFinal)

    document.getElementById("div_username").childNodes[1].childNodes[2].value = usuarioFinal
}
/*para poner la primera letra en mayuscula */
function ponerPrimeraMayuscula(str){
    return str.charAt(0).toUpperCase() + str.slice(1)

}

/*recojo los inputs y les añado el listener de alpderder el foko */
let campoNombre = document.getElementById("div_first_name")
campoNombre.childNodes[1].childNodes[3].addEventListener("blur", generarUsuario)

let campoApellido = document.getElementById("div_last_name")
campoApellido.childNodes[1].childNodes[3].addEventListener("blur", generarUsuario)
