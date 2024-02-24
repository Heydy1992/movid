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