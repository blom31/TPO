const nombre = document.getElementById("name");
const correo = document.getElementById("correo");
const contraseña = document.getElementById("pass");
const parrafo = document.getElementById("warnings");

form.addEventListener("submit", e=>{
    e.preventDefault();
    let warnings = "";
    let entrar = false;
    let regexEmail = /^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$/;
    parrafo.innerHTML = "";
    if(nombre.value.length <6){
        warnings += 'El nombre no es válido <br>';
        entrar = true;
    }
    console.log(regexEmail.test(correo.value));
    if(!regexEmail.test(correo.value)){
        warnings += 'El email no es válido <br>';
        entrar = true;
    }
    if(contraseña.value.length < 8){
        warnings += 'La contraseña no es válida <br>';
        entrar = true;
    }
    if(entrar){
        parrafo.innerHTML = warnings;
    }else{
        parrafo.innerHTML = "Enviado";
    }
})