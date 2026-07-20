var API_BASE = (function () {
  var host = window.location.hostname;
  if (host === "localhost" || host === "127.0.0.1") {
    return "http://localhost:5000/api";
  }
  return "https://travelpulse-api.onrender.com/api";
})();
