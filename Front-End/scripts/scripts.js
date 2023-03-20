const show_pswd = document.querySelector(".eye-open")
const hide_pswd = document.querySelector(".eye-close")
const login_pswd = document.querySelector("#login-password")

show_pswd.onclick = function() {
    login_pswd.type = "text";
    show_pswd.classList.add("d-none")
    hide_pswd.classList.remove("d-none")
}

hide_pswd.onclick = function() {
    login_pswd.type = "password";
    hide_pswd.classList.add("d-none")
    show_pswd.classList.remove("d-none")
}








const infoIcon = document.getElementById("info-icon");
const infoPopup = document.getElementById("info-popup");

infoIcon.addEventListener("mouseover", showInfoPopup);
infoIcon.addEventListener("mouseout", hideInfoPopup);

function showInfoPopup() {
  infoPopup.style.display = "block";
}

function hideInfoPopup() {
  infoPopup.style.display = "none";
}