// version 1
function initApp() {
    const hamburguerBtn = document.getElementById("hamburger-btn")
    const mobileMenu = document.getElementById("mobile-menu")

    function toggleMenu() {
        mobileMenu.classList.toggle("d-none")
        mobileMenu.classList.toggle("flex")
        hamburguerBtn.classList.toggle("opened-mobile-btn")
    }

    hamburguerBtn.onclick = () => {toggleMenu()}
    mobileMenu.onclick = () => {toggleMenu()}
}

document.addEventListener('DOMContentLoaded', initApp)