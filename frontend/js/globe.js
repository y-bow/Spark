var TP = window.TP || {};
window.TP = TP;

/* ──────────────────────────────────────────────────
   LOCATIONS — searchable global landmarks + countries
   ────────────────────────────────────────────────── */

var LOCATIONS = [
  // Asia
  { name: "Taj Mahal",             country: "India",       lat: 27.1751,  lng: 78.0421,  altitude: 1.4, aliases: ["agra", "taj"] },
  { name: "Great Wall of China",   country: "China",       lat: 40.4319,  lng: 116.5704, altitude: 1.6, aliases: ["great wall", "wall of china", "changcheng"] },
  { name: "Angkor Wat",            country: "Cambodia",    lat: 13.4125,  lng: 103.8670, altitude: 1.5, aliases: ["angkor", "siem reap"] },
  { name: "Mount Fuji",            country: "Japan",       lat: 35.3606,  lng: 138.7274, altitude: 1.4, aliases: ["fuji", "fujiyama", "fujisan"] },
  { name: "Petra",                 country: "Jordan",      lat: 30.3285,  lng: 35.4444,  altitude: 1.5, aliases: ["rose city", "al-Khazneh"] },
  { name: "Bali",                  country: "Indonesia",   lat: -8.3405,  lng: 115.0920, altitude: 1.4, aliases: ["island of the gods", "denpasar"] },
  { name: "Kyoto",                 country: "Japan",       lat: 35.0116,  lng: 135.7681, altitude: 1.4, aliases: ["temples", "geisha"] },
  { name: "Singapore Marina Bay",  country: "Singapore",   lat: 1.2816,   lng: 103.8636, altitude: 1.2, aliases: ["marina bay", "marina bay sands", "singapore"] },
  { name: "Ha Long Bay",           country: "Vietnam",     lat: 20.9101,  lng: 107.1839, altitude: 1.5, aliases: ["ha long", "bai tu long"] },
  { name: "Boracay",               country: "Philippines", lat: 11.9674,  lng: 121.9248, altitude: 1.4, aliases: ["white beach", "malay"] },
  { name: "Chiang Mai",            country: "Thailand",    lat: 18.7883,  lng: 98.9853,  altitude: 1.4, aliases: ["chiangmai", "northern thailand", "doi suthep"] },
  { name: "Bagan",                 country: "Myanmar",     lat: 21.1717,  lng: 94.8585,  altitude: 1.5, aliases: ["pagodas", "old bagan"] },
  { name: "Hampi",                 country: "India",       lat: 15.3350,  lng: 76.4600,  altitude: 1.4, aliases: ["vijayanagara", "virupaksha"] },

  // Europe
  { name: "Eiffel Tower",          country: "France",      lat: 48.8584,  lng: 2.2945,   altitude: 1.3, aliases: ["eiffel", "paris tower", "tour eiffel"] },
  { name: "Colosseum",             country: "Italy",       lat: 41.8902,  lng: 12.4922,  altitude: 1.4, aliases: ["rome colosseum", "flavian amphitheatre"] },
  { name: "Sagrada Familia",       country: "Spain",       lat: 41.4036,  lng: 2.1744,   altitude: 1.3, aliases: ["barcelona cathedral", "gaudi"] },
  { name: "Santorini",             country: "Greece",      lat: 36.3932,  lng: 25.4615,  altitude: 1.3, aliases: ["thira", "oia", "aegean"] },
  { name: "Big Ben",               country: "United Kingdom", lat: 51.5007, lng: -0.1246, altitude: 1.3, aliases: ["elizabeth tower", "westminster", "parliament"] },
  { name: "Acropolis",             country: "Greece",      lat: 37.9715,  lng: 23.7267,  altitude: 1.4, aliases: ["parthenon", "athens"] },
  { name: "Neuschwanstein Castle", country: "Germany",     lat: 47.5576,  lng: 10.7498,  altitude: 1.4, aliases: ["neuschwanstein", "fairy tale castle", "bavaria"] },
  { name: "St. Peter's Basilica",  country: "Vatican City", lat: 41.9022, lng: 12.4539,  altitude: 1.3, aliases: ["vatican", "peters basilica", "rome"] },
  { name: "Charles Bridge",        country: "Czech Republic", lat: 50.0865, lng: 14.4114, altitude: 1.3, aliases: ["prague bridge", "karluv most"] },

  // Americas
  { name: "Statue of Liberty",     country: "United States", lat: 40.6892, lng: -74.0445, altitude: 1.3, aliases: ["liberty", "lady liberty", "new york"] },
  { name: "Machu Picchu",          country: "Peru",        lat: -13.1631, lng: -72.5450, altitude: 1.5, aliases: ["incan citadel", "sacred valley"] },
  { name: "Christ the Redeemer",   country: "Brazil",      lat: -22.9519, lng: -43.2105, altitude: 1.3, aliases: ["cristo", "rio", "corcovado"] },
  { name: "Grand Canyon",          country: "United States", lat: 36.1069, lng: -112.1129, altitude: 1.5, aliases: ["arizona", "colorado river"] },
  { name: "Niagara Falls",         country: "Canada",      lat: 43.0896,  lng: -79.0849, altitude: 1.3, aliases: ["falls", "horseshoe falls"] },
  { name: "Chichen Itza",          country: "Mexico",      lat: 20.6843,  lng: -88.5678, altitude: 1.5, aliases: ["maya", "pyramid", "el castillo"] },
  { name: "Iguazu Falls",          country: "Argentina",   lat: -25.6953, lng: -54.4367, altitude: 1.4, aliases: ["iguazu", "iguassu", "devil's throat"] },
  { name: "Banff National Park",   country: "Canada",      lat: 51.4968,  lng: -115.9281, altitude: 1.5, aliases: ["banff", "rocky mountains", "lake louise"] },
  { name: "Torres del Paine",      country: "Chile",       lat: -50.9423, lng: -73.4068, altitude: 1.5, aliases: ["patagonia", "torres"] },

  // Africa
  { name: "Pyramids of Giza",      country: "Egypt",       lat: 29.9792,  lng: 31.1342,  altitude: 1.4, aliases: ["pyramids", "great pyramid", "giza", "sphinx"] },
  { name: "Table Mountain",        country: "South Africa", lat: -33.9628, lng: 18.4098, altitude: 1.3, aliases: ["cape town", "table"] },
  { name: "Victoria Falls",        country: "Zimbabwe",    lat: -17.9243, lng: 25.8572,  altitude: 1.5, aliases: ["mosi-oa-tunya", "livingstone"] },
  { name: "Serengeti",             country: "Tanzania",    lat: -2.3333,  lng: 34.8333,  altitude: 1.5, aliases: ["great migration", "safari"] },
  { name: "Marrakech Medina",      country: "Morocco",     lat: 31.6258,  lng: -7.9891,  altitude: 1.4, aliases: ["marrakech", "marrakesh", "jemaa el-fnaa"] },
  { name: "Cape of Good Hope",     country: "South Africa", lat: -34.3568, lng: 18.4742, altitude: 1.4, aliases: ["cape point", "cape town"] },
  { name: "Okavango Delta",        country: "Botswana",    lat: -19.5000, lng: 22.9667,  altitude: 1.5, aliases: ["okavango", "delta"] },

  // Oceania
  { name: "Sydney Opera House",    country: "Australia",   lat: -33.8568, lng: 151.2153, altitude: 1.3, aliases: ["opera house", "sydney", "harbour"] },
  { name: "Great Barrier Reef",    country: "Australia",   lat: -18.2871, lng: 147.6992, altitude: 1.5, aliases: ["barrier reef", "queensland", "coral sea"] },
  { name: "Uluru",                 country: "Australia",   lat: -25.3444, lng: 131.0369, altitude: 1.5, aliases: ["ayers rock", "red centre"] },
  { name: "Milford Sound",         country: "New Zealand", lat: -44.6414, lng: 167.8972, altitude: 1.4, aliases: ["fiordland", "piopiotahi"] },
  { name: "Bora Bora",             country: "French Polynesia", lat: -16.5004, lng: -151.7415, altitude: 1.3, aliases: ["bora", "tahiti", "lagoon"] },

  // India (key tourist spots)
  { name: "Mahabalipuram",  country: "India",  lat: 12.62,  lng: 80.19,  altitude: 1.2, aliases: ["mamallapuram", "shore temple"] },
  { name: "Madurai",        country: "India",  lat: 9.92,   lng: 78.12,  altitude: 1.2, aliases: ["temple city", "meenakshi"] },
  { name: "Ooty",           country: "India",  lat: 11.41,  lng: 76.69,  altitude: 1.2, aliases: ["ootacamund", "nilgiris"] },
  { name: "Kodaikanal",     country: "India",  lat: 10.24,  lng: 77.48,  altitude: 1.2, aliases: ["kodai", "palani hills"] },
  { name: "Rameswaram",     country: "India",  lat: 9.28,   lng: 79.31,  altitude: 1.2, aliases: ["rameshwaram", "island temple"] },
  { name: "Kanyakumari",    country: "India",  lat: 8.08,   lng: 77.53,  altitude: 1.2, aliases: ["cape comorin"] },
  { name: "Pondicherry",    country: "India",  lat: 11.94,  lng: 79.80,  altitude: 1.2, aliases: ["puducherry", "french riviera"] },
  { name: "Jaipur",         country: "India",  lat: 26.91,  lng: 75.78,  altitude: 1.2, aliases: ["pink city", "rajasthan"] },
  { name: "Goa",            country: "India",  lat: 15.29,  lng: 74.12,  altitude: 1.2, aliases: ["beaches", "portuguese"] },
  { name: "Varanasi",       country: "India",  lat: 25.31,  lng: 82.97,  altitude: 1.2, aliases: ["benares", "kashi"] },
  { name: "Kerala Backwaters", country: "India", lat: 9.49, lng: 76.33, altitude: 1.2, aliases: ["alleppey", "houseboat", "kerala"] },
];

/* ──────────────────────────────────────────────────
   Fuse.js fuzzy search setup
   ────────────────────────────────────────────────── */

var fuse = null;
if (typeof Fuse !== "undefined") {
  fuse = new Fuse(LOCATIONS, {
    keys: ["name", "aliases", "country"],
    threshold: 0.3,
    includeScore: true,
    minMatchCharLength: 2,
  });
}

/* ──────────────────────────────────────────────────
   Globe initialization
   ────────────────────────────────────────────────── */

(function () {
  var container = document.getElementById("globeViz");
  if (!container) return;

  if (typeof Globe === "undefined") {
    container.innerHTML =
      '<p class="globe-loading">Globe library failed to load. Check your connection.</p>';
    return;
  }

  var TEXTURE = "https://unpkg.com/three-globe@2.41.2/example/img/earth-blue-marble.jpg";
  var BUMP    = "https://unpkg.com/three-globe@2.41.2/example/img/earth-topology.png";

  var globe = Globe()(container)
    .globeImageUrl(TEXTURE)
    .bumpImageUrl(BUMP)
    .backgroundImageUrl("")
    .pointAltitude(0.01)
    .pointRadius(0.4)
    .pointColor(function () { return "#C9A24B"; })
    .pointLabel(function (d) {
      return (
        '<div style="padding:6px 10px;background:#161B2E;border:1px solid rgba(201,162,75,0.2);border-radius:8px;font-family:Inter,sans-serif;">' +
        '<strong style="color:#F0EAD8;font-size:13px;">' + d.name + "</strong><br/>" +
        '<span style="color:rgba(240,234,216,0.55);font-size:11px;">' + (d.country || d.region) + " &middot; " + (d.category || "") + "</span>" +
        "</div>"
      );
    })
    .arcColor(function () { return ["#1B7A6E", "#C9A24B"]; })
    .arcDashLength(0.4)
    .arcDashGap(0.2)
    .arcDashAnimateTime(1800)
    .arcStroke(0.6);

  // ── Match canvas clear color to page background — eliminates seam ──
  globe.renderer().setClearColor(0x0B0E1A, 1);

  // ── Controls: drag, zoom, auto-rotate ──
  var controls = globe.controls();
  controls.enabled = true;
  controls.enableZoom = true;
  controls.enablePan = false;
  controls.autoRotate = true;
  controls.autoRotateSpeed = 0.3;
  controls.enableDamping = true;
  controls.dampingFactor = 0.08;

  // ── Centering: explicit size + ResizeObserver ──
  function syncSize() {
    var w = container.clientWidth;
    var h = container.clientHeight;
    if (w > 0 && h > 0) {
      globe.width(w).height(h);
    }
  }
  syncSize();

  if (typeof ResizeObserver !== "undefined") {
    var ro = new ResizeObserver(syncSize);
    ro.observe(container);
  }
  window.addEventListener("resize", syncSize);

   // ── Wide view first, ease into global perspective ──
   globe.pointOfView({ lat: 20, lng: 0, altitude: 2.6 }, 0);

  // ── Auto-rotate idle detection ──
  var idleTimer = null;
  var IDLE_DELAY = 4000;

  function startIdleTimer() {
    clearTimeout(idleTimer);
    controls.autoRotate = false;
    idleTimer = setTimeout(function () {
      controls.autoRotate = true;
    }, IDLE_DELAY);
  }

  container.addEventListener("pointerdown", startIdleTimer);
  container.addEventListener("wheel", startIdleTimer);

  // ── Navigate globe to a location ──
  function navigateTo(loc) {
    startIdleTimer();
    globe.pointOfView({ lat: loc.lat, lng: loc.lng, altitude: loc.altitude || 1.4 }, 2000);

    // Pulsing ring via htmlElementsData
    globe.htmlElementsData([{
      lat: loc.lat,
      lng: loc.lng,
      id: "search-ring"
    }]);

    globe.htmlElement(function (d) {
      if (d.id !== "search-ring") return null;
      var el = document.createElement("div");
      el.className = "search-pulse";
      el.style.width = "14px";
      el.style.height = "14px";
      el.style.borderRadius = "50%";
      el.style.border = "2px solid #C9A24B";
      el.style.background = "rgba(201,162,75,0.25)";
      el.style.animation = "pulseRing 1.5s cubic-bezier(0,0,0.2,1) infinite";
      return el;
    });

    // Clear ring after 8 seconds
    setTimeout(function () {
      globe.htmlElementsData([]);
    }, 8000);
  }

  TP.searchGlobe = navigateTo;

  // ── Toast ──
  TP.showToast = function (msg) {
    var toast = document.getElementById("toast");
    if (!toast) return;
    toast.textContent = msg;
    toast.classList.add("show");
    setTimeout(function () { toast.classList.remove("show"); }, 4000);
  };

  // ── Search: fuzzy dropdown ──
  var searchInput  = document.getElementById("search-input");
  var searchForm   = document.getElementById("search-form");
  var dropdown     = document.getElementById("search-dropdown");
  var activeIdx    = -1;
  var currentResults = [];

  function closeDropdown() {
    if (dropdown) dropdown.classList.remove("open");
    activeIdx = -1;
    currentResults = [];
  }

  function renderDropdown(results) {
    if (!dropdown) return;
    if (!results.length) {
      dropdown.innerHTML = '<div class="search-dropdown-empty">No destination found &mdash; try a country or city name</div>';
      dropdown.classList.add("open");
      return;
    }
    dropdown.innerHTML = results.map(function (r, i) {
      return (
        '<div class="search-dropdown-item" data-idx="' + i + '">' +
        '<span class="match-name">' + r.item.name + '</span>' +
        '<span class="match-country">' + r.item.country + '</span>' +
        '</div>'
      );
    }).join("");
    dropdown.classList.add("open");

    // Click handlers
    dropdown.querySelectorAll(".search-dropdown-item").forEach(function (el) {
      el.addEventListener("mousedown", function (e) {
        e.preventDefault();
        var idx = parseInt(el.getAttribute("data-idx"), 10);
        selectResult(results[idx]);
      });
    });
  }

  function selectResult(result) {
    if (!result) return;
    var loc = result.item;
    searchInput.value = loc.name;
    closeDropdown();
    navigateTo(loc);

    // Highlight pins in that country if any exist
    if (TP.allDestinations && TP.allDestinations.length) {
      var countryLower = (loc.country || "").toLowerCase();
      var matchingPins = TP.allDestinations.filter(function (d) {
        return (d.country || "").toLowerCase() === countryLower;
      });
      if (matchingPins.length) {
        globe.pointsData(matchingPins.map(function (d) {
          return { lat: d.lat, lng: d.lng, name: d.name, region: d.region, country: d.country, category: d.category };
        }));
      }
    }
  }

  function handleInput() {
    var q = (searchInput.value || "").trim();
    if (q.length < 2 || !fuse) { closeDropdown(); return; }

    currentResults = fuse.search(q).slice(0, 5);
    activeIdx = -1;
    renderDropdown(currentResults);
  }

  if (searchInput) {
    // Debounced input
    var inputTimer = null;
    searchInput.addEventListener("input", function () {
      clearTimeout(inputTimer);
      inputTimer = setTimeout(handleInput, 200);
    });

    // Keyboard navigation
    searchInput.addEventListener("keydown", function (e) {
      if (!dropdown || !dropdown.classList.contains("open")) return;
      if (e.key === "ArrowDown") {
        e.preventDefault();
        activeIdx = Math.min(activeIdx + 1, currentResults.length - 1);
        highlightItem();
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        activeIdx = Math.max(activeIdx - 1, 0);
        highlightItem();
      } else if (e.key === "Enter") {
        e.preventDefault();
        if (activeIdx >= 0 && currentResults[activeIdx]) {
          selectResult(currentResults[activeIdx]);
        } else if (currentResults.length) {
          selectResult(currentResults[0]);
        }
      } else if (e.key === "Escape") {
        closeDropdown();
      }
    });

    // Close on outside click
    document.addEventListener("click", function (e) {
      if (searchInput && !searchInput.contains(e.target) && dropdown && !dropdown.contains(e.target)) {
        closeDropdown();
      }
    });
  }

  function highlightItem() {
    if (!dropdown) return;
    dropdown.querySelectorAll(".search-dropdown-item").forEach(function (el, i) {
      el.classList.toggle("active", i === activeIdx);
    });
  }

  // ── Load destinations + routes ──
  var loadingEl = document.createElement("p");
  loadingEl.className = "globe-loading";
  loadingEl.textContent = "Loading destinations\u2026";
  container.appendChild(loadingEl);

  TP.destinationsReady = fetch(API_BASE + "/destinations")
    .then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.json();
    })
    .then(function (destinations) {
      loadingEl.remove();
      TP.destinations = destinations;
      TP.allDestinations = destinations;

      globe.pointsData(
        destinations.map(function (d) {
          return {
            lat: d.lat,
            lng: d.lng,
            name: d.name,
            region: d.region,
            country: d.country,
            category: d.category,
          };
        })
      );

       // ── Smooth transition to overview after data loads ──
       setTimeout(function () {
         globe.pointOfView({ lat: 20, lng: 0, altitude: 1.6 }, 2500);
       }, 800);

      return fetch(API_BASE + "/routes");
    })
    .then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.json();
    })
    .then(function (routes) {
      globe.arcsData(
        routes.map(function (r) {
          return {
            startLat: r.origin_lat,
            startLng: r.origin_lng,
            endLat: r.dest_lat,
            endLng: r.dest_lng,
            label: r.origin + " \u2192 " + r.destination + " (" + r.mode + ")",
          };
        })
      );
    })
    .catch(function (err) {
      loadingEl.remove();
      if (container.querySelector("canvas")) {
        container.insertAdjacentHTML("afterbegin",
          '<p class="globe-loading" style="position:absolute;top:10px;left:0;right:0;text-align:center;">Couldn\u2019t load map data. Is the server running?</p>');
      } else {
        container.innerHTML =
          '<p class="globe-loading">Couldn\u2019t load map data. Is the server running?</p>';
      }
      console.error("Globe data error:", err);
    });
})();
