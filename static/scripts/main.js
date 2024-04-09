/* на будущее -- нужно будет создать два разных js */
/* для авторизованных пользователей отдельный файл, для анонимных отдельный */

document.addEventListener('DOMContentLoaded', function() {
    /* события для навигационного меню в мобильном режиме */
    let menuFixed = false;
    let menuToggle = document.getElementById('nav-toggle');
    let menu = document.getElementById('nav-left');
    menuToggle.addEventListener('mouseover', function() {
        menu.classList.add('active');
    });
    menu.addEventListener('mouseleave', function() {
        if (!menuFixed) menu.classList.remove('active');
    });
    menuToggle.addEventListener('click', function() {
        if (menuFixed) {
            menu.classList.remove('active');
        }
        else {
            menu.classList.add('active');
        }
        menuFixed = !menuFixed;
        menuToggle.firstElementChild.style.hidden=true;
    });
    document.addEventListener('click', function(event) {
        if (!menu.contains(event.target) && !menuToggle.contains(event.target)) {
            menu.classList.remove('active');
            menuFixed = false;
        }
    });

    /* события для пользователя */
    /* появляет окно пользователя по клику на иконку */
    let userIcon = document.getElementById('user-icon');
    let userApp = document.getElementById('header-user-menu');
    userIcon.addEventListener('click', function() {
        userApp.classList.toggle('active');
    });
    /* скрывает окно пользователя, если тыкаешь где-то на странице */
    document.addEventListener('click', function(event) {
        if (!userApp.contains(event.target) && event.target !== userIcon) {
            userApp.classList.remove('active');
        }
    });
});