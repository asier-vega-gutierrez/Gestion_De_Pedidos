const inputsFormulario = document.querySelectorAll("#formularioRegistro input");
const Formulario = document.getElementById('formularioRegistro');

const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,30}$/, // Letras, numeros, guion y guion_bajo
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    apellido: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	password: /^.{4,20}$/, // 4 a 20 digitos.
}

const camposFormulario = {
    username: false,
    first_name: false,
    last_name: false,
    email: false,
    password1: false
}

const validarFormulario = (e) => {
    switch (e.target.name){
        case "username":
            validarCampo(expresiones.usuario, e.target, 'Usuario');
        break;
        case "first_name":
            validarCampo(expresiones.nombre, e.target, 'Nombre');
        break;
        case "last_name":
            validarCampo(expresiones.apellido, e.target, 'Apellido');
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

const validarCampo = (expresion, input, campo ) => {
    if (expresion.test(input.value)) {
        document.getElementById(`div${campo}`).classList.remove('formulario_incorrecto');
        document.getElementById(`div${campo}`).classList.add('formulario_correcto');
        document.querySelector(`#div${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#div${campo} i`).classList.add('fa-check-circle');
        camposFormulario[campo] = true;

    } else {
        document.getElementById(`div${campo}`).classList.add('formulario_incorrecto');
        document.getElementById(`div${campo}`).classList.remove('formulario_correcto');
        document.querySelector(`#div${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#div${campo} i`).classList.add('fa-times-circle');
        camposFormulario[campo] = false;
    }
}

const validarPassword2 = () => {
    const inputPass1 = document.getElementById('id_password1');
    const inputPass2 = document.getElementById('id_password2');

    if(inputPass1.value !== inputPass2.value) {
        document.getElementById(`divPassword2`).classList.add('formulario_incorrecto');
        document.getElementById(`divPassword2`).classList.remove('formulario_correcto');
        document.querySelector(`#divPassword2 i`).classList.remove('fa-check-circle');
        document.querySelector(`#divPassword2 i`).classList.add('fa-times-circle');
        camposFormulario['Password1'] = false;
    } else {
        document.getElementById(`divPassword2`).classList.remove('formulario_incorrecto');
        document.getElementById(`divPassword2`).classList.add('formulario_correcto');
        document.querySelector(`#divPassword2 i`).classList.remove('fa-times-circle');
        document.querySelector(`#divPassword2 i`).classList.add('fa-check-circle');
        camposFormulario['Password1'] = true;
    }
}

inputsFormulario.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});

Formulario.addEventListener('submit', (e) => {
    if (camposFormulario.username && camposFormulario.first_name && camposFormulario.last_name && camposFormulario.email && camposFormulario.password1) {

    } else {
        alert('Alguno de los campos no era correcto. Por favor, vuelva a intentarlo');
        Formulario.reset();
    }

});