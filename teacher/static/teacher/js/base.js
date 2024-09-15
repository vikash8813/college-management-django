const navbtn = document.querySelector('.toggle')
const sidebar = document.querySelector('.sidebar')
const main = document.querySelector('.main')


navbtn.addEventListener('click', () => {
    sidebar.classList.toggle('close');
    main.classList.toggle('close');
    navbtn.classList.toggle('cls');
    document.getElementsByClassName("myaclass").style.padding = "0px";
})