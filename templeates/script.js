const backgrounds = [
    "/imagenes/fondo1.png",
    "/imagenes/fondo2.png",
    "/imagenes/fondo3.png"
];

let current = 0;

function changeBackground() {
    const hero = document.querySelector(".hero");

    // Aplicar la clase de desvanecimiento
    hero.classList.add("fade");

    setTimeout(() => {
        // Cambiar la imagen cuando ya está desvanecido
        current = (current + 1) % backgrounds.length;
        hero.style.backgroundImage = `url(${backgrounds[current]})`;

        // Volvver a hacer visible el fondo
        hero.classList.remove("fade");
    }, 500); // El cambio ocurre en 500ms, asegurando que no haya doble parpadeo
}

// Cambia cada 3 segundos
setInterval(changeBackground, 3000);
