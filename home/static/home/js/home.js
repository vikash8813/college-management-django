
var w= window.innerWidth
new_w=parseInt(w)

window.onload = function() {anime()};

function anime(){
  if(new_w>800){
    document.querySelector('.chnc-box'). setAttribute('data-aos', 'fade-right');
    document.querySelector('.scroll-box'). setAttribute('data-aos', 'fade-left');
    document.querySelector('.cran'). setAttribute('data-aos', 'fade-right');
    document.querySelector('.study-course'). setAttribute('data-aos', 'fade-left');
  }
}




var swiper = new Swiper(".mySwiper", {
    slidesPerView: 'auto',
    spaceBetween: 30,
    speed:600,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
});


document.querySelector("#scroll-container").addEventListener('mouseover', function() {
	document.querySelector("#scroll-text").style.animationPlayState = 'paused';
});

document.querySelector("#scroll-container").addEventListener('mouseout', function() {
	document.querySelector("#scroll-text").style.animationPlayState = 'running';
});


