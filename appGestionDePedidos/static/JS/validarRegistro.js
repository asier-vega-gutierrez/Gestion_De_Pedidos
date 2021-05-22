/*Creamos la constante inputsFormulario, para reunir todos los inputs del formulario*/
const inputsFormulario = document.querySelectorAll("#formularioRegistro input");
/*Creamos la constante Formulario, para hacer referencia al formulario*/
const Formulario = document.getElementById('formularioRegistro');

/*Creamos la constante expresiones, para establecer un modelo a seguir por input*/
const expresiones = {
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    apellido: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    usuario: /^[a-zA-Z0-9\_\-]{4,30}$/, // Letras, numeros, guion y guion_bajo
    email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/, //Formato email
	password: /^.{4,20}$/, // 4 a 20 digitos.
}

/*Creamos la constante camposFormulario, para validar pasando a true, el campo que cumpla las condiciones*/
const camposFormulario = {
    first_name: false,
    last_name: false,
    username: false,
    email: false,
    password1: false
}

/*Creamos la funcion de tipo arrow validarFormulario, que llama a la funcion validarCampo de una manera automatica, independientemente del campo*/
const validarFormulario = (e) => {
    /*Switch para elegir el campo adecuado en cada caso, dependiendo el case*/
    switch (e.target.name){
        /*Campo del nombre del usuario*/
        case "first_name":
            validarCampo(expresiones.nombre, e.target, 'first_name');
        break;
        /*Campo del apellido del usuario*/
        case "last_name":
            validarCampo(expresiones.apellido, e.target, 'last_name');
        break;
        /*Campo del nombre del usuario a crear*/
        case "username":
            validarCampo(expresiones.usuario, e.target, 'username');
        break;
        /*Campo del email del usuario*/
        case "email":
            validarCampo(expresiones.email, e.target, 'email');
        break;
        /*Campo de la contraseña de la cuenta*/
        case "password1":
            validarCampo(expresiones.password, e.target, 'password1');
            validarPassword2();
        break;
        /*Comprobacion de la contraseña de la cuenta*/
        case "password2":
            validarPassword2();
        break;
    }
}

/*Creamos la funcion de tipo arrow validarCampo, que añade o elimina una clase al div de dicho campo con el fin de mostra un determinado icono y validar los campos*/
const validarCampo = (expresion, input, campo ) => {
    if (expresion.test(input.value)) {
        document.getElementById(`div_${campo}`).classList.remove('formulario_incorrecto');
        document.getElementById(`div_${campo}`).classList.add('formulario_correcto');
        document.querySelector(`#div_${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#div_${campo} i`).classList.add('fa-check-circle');
        camposFormulario[campo] = true;

    } else {
        document.getElementById(`div_${campo}`).classList.add('formulario_incorrecto');
        document.getElementById(`div_${campo}`).classList.remove('formulario_correcto');
        document.querySelector(`#div_${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#div_${campo} i`).classList.add('fa-times-circle');
        camposFormulario[campo] = false;
    }
}

//*Creamos la funcion de tipo arrow validarPassword2, para validar que la password1 es igual a la password 2 en todo momento*/
const validarPassword2 = () => {
    const inputPass1 = document.getElementById('id_password1');
    const inputPass2 = document.getElementById('id_password2');

    if(inputPass1.value !== inputPass2.value) {
        document.getElementById(`div_password2`).classList.add('formulario_incorrecto');
        document.getElementById(`div_password2`).classList.remove('formulario_correcto');
        document.querySelector(`#div_password2 i`).classList.remove('fa-check-circle');
        document.querySelector(`#div_password2 i`).classList.add('fa-times-circle');

        camposFormulario['password1'] = false;
    } else {
        document.getElementById(`div_password2`).classList.remove('formulario_incorrecto');
        document.getElementById(`div_password2`).classList.add('formulario_correcto');
        document.querySelector(`#div_password2 i`).classList.remove('fa-times-circle');
        document.querySelector(`#div_password2 i`).classList.add('fa-check-circle');
        camposFormulario['password1'] = true;
    }
}

/*Recorremos con el forEach todos cada input de la constante inputsFormualrio, y añadimos 2 EventListeners*/
inputsFormulario.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});

/*Añadimos un EventListener al formulario para que no permita enviar los datos si la validacion no es correcta*/
Formulario.addEventListener('submit', (e) => {
    if (camposFormulario.username && camposFormulario.first_name && camposFormulario.last_name && camposFormulario.email && camposFormulario.password1 == true) {

    } else {
        alert('Alguno de los campos no era correcto. Por favor, vuelva a intentarlo');
        Formulario.reset();
    }
});