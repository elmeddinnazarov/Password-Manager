const sing_in = document.querySelector(".sign-in");
const sing_up = document.querySelector(".sign-up");
const singup_btn = document.querySelector(".sign_up_now");
const singin_btn = document.querySelector(".sign_in_now");
const goSignIn = document.querySelector(".go-to-login");
const conf_menu = document.querySelector(".confirmation");
const register_submit = document.querySelector("#register-submit");

singup_btn.onclick = function() {
    make_unvisible(sing_in);
    make_visible(sing_up); 
}

singin_btn.onclick = function() {
    make_unvisible(sing_up);
    make_visible(sing_in); 
}

goSignIn.onclick = function() {
    make_unvisible(conf_menu);
    make_visible(sing_in); 
}

register_submit.onclick = function() {
    make_unvisible(sing_up);
    make_visible(conf_menu); 
}

function make_unvisible(target) {
    switch (target) {
        case sing_in:
            animate(target, "m_unvisible_in", "top", 130+"%");
            break;
        case conf_menu:
            animate(target, "m_unvisible_conf", "transform", "scale(0)");
            break;
        default:
            animate(target, "m_unvisible_up", "top", "-"+99+"%");
    }
}

function make_visible(target) {
    switch (target) {
        case sing_in:
            animate(target, "m_visible_in", "top", 0+"%");
            break;
        case conf_menu:
            animate(target, "m_visible_conf", "transform", "scale(1)");
            break;
        default:
            animate(target, "m_visible_up", "top", 0+"%");
    }
}

function animate(target, animationName, property, value) {
    target.style.animation = animationName + " 1s";
    setTimeout(() => {
        target.style[property] = value;
        target.style.removeProperty('animation');
    }, 900);
}