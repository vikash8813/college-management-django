var w= window.innerWidth
new_w=parseInt(w)

window.onload = function() {anime()};

function anime(){
  if(new_w>800){

    document.querySelectorAll('.about-image')[0]. setAttribute('data-aos', 'fade-right');
    document.querySelectorAll('.about-text')[0]. setAttribute('data-aos', 'fade-left');
    document.querySelectorAll('.about-image')[1]. setAttribute('data-aos', 'fade-left');
    document.querySelectorAll('.about-text')[1]. setAttribute('data-aos', 'fade-right');

  }
}
