(function () {
  var token = localStorage.getItem("token");
  var navLinks = document.querySelector(".nav-links");
  if (!navLinks) return;

  var loginLink = navLinks.querySelector('a[href*="login"]');
  if (!loginLink) return;

  var isSubPage = window.location.pathname.indexOf("/pages/") !== -1;

  if (token) {
    loginLink.textContent = "Logout";
    loginLink.href = "#";
    loginLink.classList.remove("active");
    loginLink.classList.add("logout-link");
    loginLink.addEventListener("click", function (e) {
      e.preventDefault();
      localStorage.removeItem("token");
      window.location.href = isSubPage ? "login.html" : "pages/login.html";
    });
  }
})();
