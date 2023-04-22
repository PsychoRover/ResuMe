$(document).ready(function () {
  const images = $("#team-images img");
  let i = 0;
  setInterval(function () {
    images.eq(i).fadeOut(1000);
    i = (i + 1) % images.length;
    images.eq(i).fadeIn(1000);
  }, 3000);
});
