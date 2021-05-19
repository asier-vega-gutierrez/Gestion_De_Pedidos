const formulario = document.getElementById("formularioRegistro");
const inputUsername = document.getElementsByName('username');
const inputName = document.getElementsByName('first_name');
const inputLastname = document.getElementsByName('last_name');
const inputEmail = document.getElementsByName('email');
const inputPassword1 = document.getElementsByName('password1');
const inputPassword2 = document.getElementsByName('password2');
const inputSelect = document.getElementsByName('group');



inputEmail.addEventListener('keyup',console.log("funciona"));