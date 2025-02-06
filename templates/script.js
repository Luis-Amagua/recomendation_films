document.addEventListener("DOMContentLoaded", function () {
    // Aplicar efecto de fade-in a las películas recomendadas
    const recommendations = document.querySelectorAll("li");
    recommendations.forEach((item, index) => {
        setTimeout(() => {
            item.style.opacity = "1";
            item.style.transform = "translateY(0)";
        }, index * 300);
    });

    // Resaltar el botón al hacer hover
    const buttons = document.querySelectorAll("button");
    buttons.forEach(button => {
        button.addEventListener("mouseover", function () {
            this.style.boxShadow = "0px 0px 15px rgba(255, 0, 0, 0.8)";
        });
        button.addEventListener("mouseout", function () {
            this.style.boxShadow = "none";
        });
    });

    // Cambiar dinámicamente el fondo cuando se seleccione un género o perfil de usuario
    const selectElements = document.querySelectorAll("select");
    selectElements.forEach(select => {
        select.addEventListener("change", function () {
            document.body.style.background = "linear-gradient(to bottom, #000, #E50914)";
        });
    });
});
