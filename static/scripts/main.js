/* появляет выпадающее меню пользователя в шапке */
function OpenUserMenu(id) {
    let elem = document.getElementById(id);
    (elem.style.display !== 'block') ? (elem.style.display = 'block') : (elem.style.display = '');
}
/* скрывает меню пользователя, если тыкаешь где-то на странице */
window.onclick = function(event) {
    if (!event.target.matches('.header-dropdown-button span')) {
        let dropdownApps = document.getElementsByClassName('header-dropdown-content');
        for (let i = 0; i < dropdownApps.length; i++) {
            let openDropdown = dropdownApps[i];
            if (openDropdown.style.display === 'block' ) {
                openDropdown.style.display = 'none';
            }
        }
    }
}