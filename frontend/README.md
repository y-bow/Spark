# TravelPulse Frontend

Static frontend for the TravelPulse global travel dashboard.

## Deployment

This is a static site deployed to **Netlify**.

1. Update `js/config.js` with your Render backend URL.
2. Push to GitHub and connect the `frontend/` folder in Netlify.
3. Set publish directory to `.` in Netlify build settings.

## Structure

- `index.html` — Landing page with interactive globe
- `pages/destinations.html` — Browse all destinations (filterable catalog)
- `pages/bookings.html` — View your bookings (requires login)
- `pages/login.html` — Login and registration
- `404.html` — Styled not-found page
- `js/globe.js` — globe.gl initialization
- `js/main.js` — Destination card rendering
- `js/config.js` — API base URL constant
- `css/main.css` — Dark cinematic travel theme
