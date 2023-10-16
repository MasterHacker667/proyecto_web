const btnLogin = document.getElementById("login");
const btnRegistro = document.getElementById("registro");
const formLoginn = document.querySelector(".loginn");
const formRegister = document.querySelector(".register");

btnLogin.addEventListener("click", e => {
    formRegister.classList.add("hide");
    formLoginn.classList.remove("hide");
});

btnRegistro.addEventListener("click", e => {
    formLoginn.classList.add("hide");
    formRegister.classList.remove("hide");
});
