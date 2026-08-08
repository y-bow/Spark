(function () {
  var container = document.getElementById("destination-cards");
  if (!container) return;

  var catSelect = document.getElementById("filter-category");
  var countrySelect = document.getElementById("filter-country");
  var searchInput = document.getElementById("filter-search");
  var allData = [];

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
      container.innerHTML =
        '<div class="empty-state-container">' +
        '<div class="empty-state-icon">&#128269;</div>' +
        '<p class="empty-state">No destinations found.</p>' +
        '<p class="empty-state-hint">Try removing some filters or broadening your search.</p>' +
        '<button class="btn btn-outline" id="clear-filters-btn">Clear All Filters</button>' +
        '</div>';
      var clearBtn = document.getElementById("clear-filters-btn");
      if (clearBtn) {
        clearBtn.addEventListener("click", function () {
          if (catSelect) catSelect.value = "";
          if (countrySelect) countrySelect.value = "";
          if (searchInput) searchInput.value = "";
          renderCards(allData);
        });
      }
      observeReveals();
      return;
    }
    container.innerHTML = destinations
      .map(function (d, i) {
        var imgHtml = d.image_url
          ? '<img class="dest-card-img" src="' + d.image_url + '" alt="' + d.name + (d.region ? ' - ' + d.region : '') + ' destination overview" loading="lazy" width="400" height="225" onerror="this.onerror=null;this.src=\'/img/dest-placeholder.svg\'">'
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
          '<article class="dest-card reveal-card" style="--stagger-delay:' + (Math.min(i, 12) * 30) + 'ms">' +
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

  function renderCards(list) {
    render(list);
  }

  function populateFilters() {
    if (!catSelect || !countrySelect) return;
    var cats = {};
    var countries = {};
    allData.forEach(function (d) {
      if (d.category) cats[d.category] = true;
      if (d.country) countries[d.country] = true;
    });
    Object.keys(cats).sort().forEach(function (c) {
      var opt = document.createElement("option");
      opt.value = c;
      opt.textContent = c.charAt(0).toUpperCase() + c.slice(1);
      catSelect.appendChild(opt);
    });
    Object.keys(countries).sort().forEach(function (c) {
      var opt = document.createElement("option");
      opt.value = c;
      opt.textContent = c;
      countrySelect.appendChild(opt);
    });
  }

  function applyFilters() {
    var cat = (catSelect && catSelect.value || "").toLowerCase();
    var country = (countrySelect && countrySelect.value || "").toLowerCase();
    var q = (searchInput && searchInput.value || "").toLowerCase().trim();

    var filtered = allData.filter(function (d) {
      if (cat && (d.category || "").toLowerCase() !== cat) return false;
      if (country && (d.country || "").toLowerCase() !== country) return false;
      if (q) {
        var haystack = (
          (d.name || "") + " " +
          (d.region || "") + " " +
          (d.country || "") + " " +
          (d.description || "") + " " +
          (d.category || "") + " " +
          (d.highlights || "")
        ).toLowerCase();
        return haystack.indexOf(q) !== -1;
      }
      return true;
    });
    renderCards(filtered);
  }

  if (catSelect) catSelect.addEventListener("change", applyFilters);
  if (countrySelect) countrySelect.addEventListener("change", applyFilters);
  if (searchInput) {
    var searchTimer = null;
    searchInput.addEventListener("input", function () {
      clearTimeout(searchTimer);
      searchTimer = setTimeout(applyFilters, 150);
    });
  }

  function observeReveals() {
    var targets = document.querySelectorAll(".reveal-card:not(.visible), .reveal:not(.visible), .reveal-eyebrow:not(.visible)");
    if (!targets.length) return;
    if (typeof IntersectionObserver === "undefined") {
      targets.forEach(function (el) { el.classList.add("visible"); });
      return;
    }
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.05, rootMargin: "0px 0px 30px 0px" });
    targets.forEach(function (el) { observer.observe(el); });
  }

  skeletonCards(6);

  if (window.TP && TP.destinations) {
    allData = TP.destinations;
    populateFilters();
    renderCards(allData);
    observeReveals();
    return;
  }

  if (window.TP && TP.destinationsReady) {
    TP.destinationsReady
      .then(function () {
        allData = TP.destinations || [];
        populateFilters();
        renderCards(allData);
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
      allData = data;
      if (window.TP) TP.destinations = data;
      populateFilters();
      renderCards(allData);
    })
    .catch(function (err) {
      container.innerHTML =
        '<p class="msg msg-error">Couldn\u2019t load destinations. Is the server running?</p>';
      console.error("Destinations error:", err);
    });

  observeReveals();
})();
