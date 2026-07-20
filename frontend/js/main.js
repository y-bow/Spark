(function () {
  var container = document.getElementById("destination-cards");
  if (!container) return;

  function skeletonCards(count) {
    var html = "";
    for (var i = 0; i < count; i++) {
      html +=
        '<article class="dest-card skeleton-card" aria-hidden="true">' +
        '<div class="skeleton-img shimmer"></div>' +
        '<div class="dest-card-body">' +
        '<div class="skeleton-line skeleton-line-sm shimmer"></div>' +
        '<div class="skeleton-line skeleton-line-lg shimmer"></div>' +
        '<div class="skeleton-line skeleton-line-md shimmer"></div>' +
        '<div class="skeleton-line skeleton-line-full shimmer"></div>' +
        '<div class="skeleton-line skeleton-line-full shimmer"></div>' +
        '</div></article>';
    }
    container.innerHTML = html;
  }

  function render(destinations) {
    if (!destinations || !destinations.length) {
      container.innerHTML = '<p class="empty-state">No destinations available.</p>';
      return;
    }
    container.innerHTML = destinations
      .map(function (d, i) {
        var imgHtml = d.image_url
          ? '<img class="dest-card-img" src="' + d.image_url + '" alt="' + d.name + '" loading="lazy" width="400" height="225">'
          : "";
        var ratingHtml = d.rating
          ? '<span class="dest-card-rating">&#9733; ' + d.rating + "</span>"
          : "";
        var feeHtml = d.entry_fee_display
          ? '<span class="dest-card-fee">' + d.entry_fee_display + "</span>"
          : "";
        var timeHtml = d.best_time_to_visit
          ? '<span class="dest-card-time">' + d.best_time_to_visit + "</span>"
          : "";
        var highlightsHtml = d.highlights
          ? '<div class="dest-card-highlights">' +
            d.highlights.split(",").map(function (h) {
              return '<span class="highlight-tag">' + h.trim() + "</span>";
            }).join("") +
            "</div>"
          : "";

        return (
          '<article class="dest-card reveal-card" style="--stagger-delay:' + (i * 60) + 'ms">' +
          imgHtml +
          '<div class="dest-card-body">' +
          '<span class="eyebrow-label">' + (d.category || "Destination") + "</span>" +
          '<div class="dest-card-title-row">' +
          "<h3>" + d.name + "</h3>" +
          ratingHtml +
          "</div>" +
          '<span class="region">' + (d.country ? d.country + " \u00b7 " + d.region : d.region) + "</span>" +
          "<p>" + (d.description || "") + "</p>" +
          (feeHtml || timeHtml
            ? '<div class="dest-card-meta">' + feeHtml + timeHtml + "</div>"
            : "") +
          highlightsHtml +
          "</div>" +
          "</article>"
        );
      })
      .join("");
    observeReveals();
  }

  function observeReveals() {
    if (typeof IntersectionObserver === "undefined") {
      var els = document.querySelectorAll(".reveal, .reveal-eyebrow, .reveal-card");
      for (var i = 0; i < els.length; i++) els[i].classList.add("visible");
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
    );

    var targets = document.querySelectorAll(".reveal, .reveal-eyebrow, .reveal-card");
    targets.forEach(function (el) { observer.observe(el); });
  }

  skeletonCards(6);

  if (window.TP && TP.destinations) {
    render(TP.destinations);
    observeReveals();
    return;
  }

  if (window.TP && TP.destinationsReady) {
    TP.destinationsReady
      .then(function () {
        render(TP.destinations || []);
      })
      .catch(function (err) {
        container.innerHTML =
          '<p class="msg msg-error">Couldn\u2019t load destinations. Is the server running?</p>';
        console.error("Destinations error:", err);
      });
    observeReveals();
    return;
  }

  fetch(API_BASE + "/destinations")
    .then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.json();
    })
    .then(function (data) {
      if (window.TP) TP.destinations = data;
      render(data);
    })
    .catch(function (err) {
      container.innerHTML =
        '<p class="msg msg-error">Couldn\u2019t load destinations. Is the server running?</p>';
      console.error("Destinations error:", err);
    });

  observeReveals();
})();
