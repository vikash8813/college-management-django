const navbtn=document.querySelector('.nav-btns')
const deksnav=document.querySelector('.deks-nav')


navbtn.addEventListener('click',()=>{
    navbtn.classList.toggle('nav-open')
    deksnav.classList.toggle('deks-nav-open')
})



window.onscroll = function() {scrollFunction()};

function scrollFunction() {
      
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.querySelector(".nav-links").style.height  = "8rem";
    document.querySelector(".mobile-nav").style.height  = "6rem";
    document.querySelector(".deks-logo-img").style.height  = "6rem";
    document.querySelector(".deks-logo-img").style.width  = "6rem";

    }
    else {
    document.querySelector(".nav-links").style.height = "10rem";
    document.querySelector(".mobile-nav").style.height = "8rem";
    document.querySelector(".deks-logo-img").style.height  = "8rem";
    document.querySelector(".deks-logo-img").style.width  = "8rem";
  }
}



