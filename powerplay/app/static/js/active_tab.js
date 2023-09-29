// Select active tab on page load
document.addEventListener("turbo:load", function() {
  const currentPath = window.location.href
  document.querySelectorAll(".sticky-footer__item").forEach(function(o, i){
    if(currentPath.includes(o.href)){
      o.classList.add("active")
    }else{
      o.classList.remove("active")
    }
  })
});
