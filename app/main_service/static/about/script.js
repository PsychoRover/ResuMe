document.addEventListener("DOMContentLoaded", function () {
  const images = document.querySelectorAll("#team-images img");
  let i = 0;
  setInterval(function () {
    images[i].classList.remove("fadeIn");
    images[i].classList.add("fadeOut");
    i = (i + 1) % images.length;
    images[i].classList.remove("fadeOut");
    images[i].classList.add("fadeIn");
  }, 3000);
});
