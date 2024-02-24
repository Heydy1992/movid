document.addEventListener('DOMContentLoaded', function() {
    
    const menuLinks = document.querySelectorAll('.menu-op');

    
    menuLinks.forEach(function(menuLink) {
      menuLink.addEventListener('click', function(event) {
        event.preventDefault(); 
  
        
        const pageName = this.textContent;
  
       
        alert(`Aquí debería ir la página "${pageName}"`);
      });
    });
  });




var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  const slides = document.querySelectorAll(".slider");
  
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  
  slideIndex++;
  
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }    
  
  slides[slideIndex - 1].style.display = "block";  
  setTimeout(showSlides, 2000); // Cambia la imagen cada 2 segundos (2000 milisegundos)
}