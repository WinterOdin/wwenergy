const doc = document;
const menuOpen = doc.querySelector(".menu");
const menuClose = doc.querySelector(".close");
const overlay = doc.querySelector(".overlay");
const buttons = doc.querySelectorAll(".linkNavMobile");

menuOpen.addEventListener("click", () => {
  overlay.classList.add("overlay--active");
});

menuClose.addEventListener("click", () => {
  overlay.classList.remove("overlay--active");
});

for (const button of buttons) {
  button.addEventListener("click", () => {
    overlay.classList.remove("overlay--active");
  });
}


(function($) {

$(".open").hide();
$('.faqQuestion ').click(function(){
  $(this).next().slideToggle();
});

})(jQuery);
