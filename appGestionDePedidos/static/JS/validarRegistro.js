/*Creamos la constante inputsFormulario, para reunir todos los inputs del formulario*/
const inputsFormulario = document.querySelectorAll("#formularioRegistro input");
/*Creamos la constante Formulario, para hacer referencia al formulario*/
const Formulario = document.getElementById('formularioRegistro');

/*Creamos la constante expresiones, para establecer un modelo a seguir por input*/
const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,30}$/, // Letras, numeros, guion y guion_bajo
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    apellido: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	password: /^.{4,20}$/, // 4 a 20 digitos.
}

/*Creamos la constante camposFormulario, para validar pasando a true, el campo que cumpla las condiciones*/
const camposFormulario = {
    username: false,
    first_name: false,
    last_name: false,
    email: false,
    password1: false
}

/*Creamos la funcion de tipo arrow validarFormulario, que llama a la funcion validarCampo de una manera automatica, independientemente del campo*/
const validarFormulario = (e) => {
    switch (e.target.name){

        case "first_name":
            validarCampo(expresiones.nombre, e.target, 'Nombre');
        break;
        case "last_name":
            validarCampo(expresiones.apellido, e.target, 'Apellido');
        break;
        case "username":
            validarCampo(expresiones.usuario, e.target, 'Usuario');
        break;
        case "email":
            validarCampo(expresiones.email, e.target, 'Email');
        break;
        case "password1":
            validarCampo(expresiones.password, e.target, 'Password1');
            validarPassword2();
        break;
        case "password2":
            validarPassword2();
        break;
    }
}

/*Creamos la funcion de tipo arrow validarCampo, que añade o elimina una clase al div de dicho campo con el fin de mostra un determinado icono*/
const validarCampo = (expresion, input, campo ) => {
    if (expresion.test(input.value)) {
        document.getElementById(`div${campo}`).classList.remove('formulario_incorrecto');
        document.getElementById(`div${campo}`).classList.add('formulario_correcto');
        document.querySelector(`#div${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#div${campo} i`).classList.add('fa-check-circle');

    } else {
        document.getElementById(`div${campo}`).classList.add('formulario_incorrecto');
        document.getElementById(`div${campo}`).classList.remove('formulario_correcto');
        document.querySelector(`#div${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#div${campo} i`).classList.add('fa-times-circle');
    }
}

//*Creamos la funcion de tipo arrow validarPassword2,, para validar que la password1 es igual a la password 2 en todo momento*/
const validarPassword2 = () => {
    const inputPass1 = document.getElementById('id_password1');
    const inputPass2 = document.getElementById('id_password2');

    if(inputPass1.value !== inputPass2.value) {
        document.getElementById(`divPassword2`).classList.add('formulario_incorrecto');
        document.getElementById(`divPassword2`).classList.remove('formulario_correcto');
        document.querySelector(`#divPassword2 i`).classList.remove('fa-check-circle');
        document.querySelector(`#divPassword2 i`).classList.add('fa-times-circle');
        camposFormulario['password1'] = false;
    } else {
        document.getElementById(`divPassword2`).classList.remove('formulario_incorrecto');
        document.getElementById(`divPassword2`).classList.add('formulario_correcto');
        document.querySelector(`#divPassword2 i`).classList.remove('fa-times-circle');
        document.querySelector(`#divPassword2 i`).classList.add('fa-check-circle');
        camposFormulario['password1'] = true;
    }
}

/*Recorremos con el forEach todos cada input de la constante inputsFormualrio, y añadimos 2 EventListeners*/
inputsFormulario.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});

/*Añadimos un EventListener al formulario para que no permita enviar los datos si la validacion no es correcta*/
Formulario.addEventListener('submit', prueba)

function prueba(){
    console.log('hola')
}
/*, (e) => {
    if (camposFormulario.username && camposFormulario.first_name && camposFormulario.last_name && camposFormulario.email && camposFormulario.password1) {

    } else {
        alert('Alguno de los campos no era correcto. Por favor, vuelva a intentarlo');
        Formulario.reset();
    }
});*/