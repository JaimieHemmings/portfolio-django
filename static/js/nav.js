document.addEventListener("DOMContentLoaded", function () {
  const navToggle = document.querySelector("#nav_toggle");
  const navContent = document.querySelector("#nav_content");

  function toggleNav() {
    navContent.classList.toggle("hidden");
  }

  navToggle.addEventListener("click", toggleNav);
  const detailsArray = document.querySelectorAll("details");
  function toggleDetails(e) {
    e.target.classList.toggle("open");
  }
  detailsArray.forEach((el) => el.addEventListener("toggle", toggleDetails));
});
