const sing_in = document.querySelector(".sign-in")
const sing_up = document.querySelector(".sign-up")
const singup_btn = document.querySelector(".sign_up_now")
const singin_btn = document.querySelector(".sign_in_now")

singup_btn.onclick = function() {
    make_unvisible(sing_in);
    make_visible(sing_up); 
}
singin_btn.onclick = function() {
    make_unvisible(sing_up);
    make_visible(sing_in); 
}

function make_unvisible(target) {
    if (target === sing_in) {
        target.style.animation = "m_unvisible_in 1s";
        setTimeout(() => {
            target.style.top = 130+"%"
            target.style.removeProperty('animation')
        }, 900);
    } else {
        target.style.animation = "m_unvisible_up 1s";
        setTimeout(() => {
            target.style.top = "-"+99+"%"
            target.style.removeProperty('animation')
        }, 900);
    }
}

function make_visible(target) {
    if (target === sing_in) {
        target.style.animation = "m_visible_in 1s";
        setTimeout(() => {
            target.style.top = 0+"%"
            target.style.removeProperty('animation')
        }, 900);
    } else {
        target.style.animation = "m_visible_up 1s";
        setTimeout(() => {
            target.style.top = 0+"%"
            target.style.removeProperty('animation')
        }, 900);
    }
}