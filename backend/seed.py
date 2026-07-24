from app import create_app
from extensions import db
from models.destination import Destination
from models.route import Route, TravelMode

DESTINATIONS = [
    {"name": "Mahabalipuram", "region": "Tamil Nadu", "country": "India", "lat": 12.6269, "lng": 80.1922, "description": "UNESCO-listed shore temples and ancient rock carvings on the Coromandel Coast.", "category": "heritage", "best_time_to_visit": "November to February", "entry_fee_display": "₹40", "rating": 4.6, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Shore Temple, Five Rathas, Tiger Cave"},
    {"name": "Madurai", "region": "Tamil Nadu", "country": "India", "lat": 9.9252, "lng": 78.1198, "description": "One of the oldest living cities, famed for the breathtaking Meenakshi Amman Temple.", "category": "heritage", "best_time_to_visit": "October to March", "entry_fee_display": "Free", "rating": 4.7, "image_url": "https://images.unsplash.com/photo-1585155966850-c8b34424999c?q=80&w=1000&auto=format&fit=crop", "highlights": "Meenakshi Amman Temple, Thirumalai Nayakkar Mahal, Banana Market"},
    {"name": "Ooty", "region": "Tamil Nadu", "country": "India", "lat": 11.4102, "lng": 76.6950, "description": "A charming hill station in the Nilgiri Hills, surrounded by tea plantations.", "category": "hillstation", "best_time_to_visit": "April to June", "entry_fee_display": "Varies", "rating": 4.5, "image_url": "https://images.unsplash.com/photo-1590050752117-23aae2ef3a27?q=80&w=1000&auto=format&fit=crop", "highlights": "Botanical Gardens, Nilgiri Mountain Railway, Rose Garden"},
    {"name": "Kodaikanal", "region": "Tamil Nadu", "country": "India", "lat": 10.2413, "lng": 77.4863, "description": "The Princess of Hill Stations, known for its misty lakes and pine forests.", "category": "hillstation", "best_time_to_visit": "April to June", "entry_fee_display": "Varies", "rating": 4.6, "image_url": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?q=80&w=1000&auto=format&fit=crop", "highlights": "Kodai Lake, Pillar Rocks, Coaker's Walk"},
    {"name": "Rameswaram", "region": "Tamil Nadu", "country": "India", "lat": 9.2876, "lng": 79.3129, "description": "Sacred island pilgrimage site connected to the Ramayana, with the stunning Pamban Bridge.", "category": "pilgrimage", "best_time_to_visit": "October to March", "entry_fee_display": "Free", "rating": 4.7, "image_url": "https://images.unsplash.com/photo-1590732487833-9489f693b221?q=80&w=1000&auto=format&fit=crop", "highlights": "Ramanathaswamy Temple, Pamban Bridge, Dhanushkodi"},
    {"name": "Kanyakumari", "region": "Tamil Nadu", "country": "India", "lat": 8.0883, "lng": 77.5385, "description": "The southernmost tip of India where three oceans meet, famous for sunrise views.", "category": "heritage", "best_time_to_visit": "October to March", "entry_fee_display": "Free", "rating": 4.6, "image_url": "https://images.unsplash.com/photo-1621323292439-989799583350?q=80&w=1000&auto=format&fit=crop", "highlights": "Vivekananda Rock Memorial, Thiruvalluvar Statue, Sunset Point"},
    {"name": "Pondicherry", "region": "Tamil Nadu", "country": "India", "lat": 11.9416, "lng": 79.8083, "description": "A coastal town with French colonial charm, vibrant cafés, and serene beaches.", "category": "heritage", "best_time_to_visit": "October to March", "entry_fee_display": "Free", "rating": 4.5, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "French Quarter, Promenade Beach, Auroville"},
    {"name": "Jaipur", "region": "Rajasthan", "country": "India", "lat": 26.9124, "lng": 75.7873, "description": "The Pink City of India, home to majestic forts and palaces.", "category": "heritage", "best_time_to_visit": "October to March", "entry_fee_display": "₹200", "rating": 4.7, "image_url": "https://images.unsplash.com/photo-1477587458883-47145ed94245?q=80&w=1000&auto=format&fit=crop", "highlights": "Amber Fort, Hawa Mahal, City Palace"},
    {"name": "Goa", "region": "Goa", "country": "India", "lat": 15.2993, "lng": 74.1240, "description": "India's beach paradise with Portuguese heritage, nightlife, and spice plantations.", "category": "island", "best_time_to_visit": "November to February", "entry_fee_display": "Free", "rating": 4.5, "image_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?q=80&w=1000&auto=format&fit=crop", "highlights": "Baga Beach, Old Goa Churches, Dudhsagar Falls"},
    {"name": "Varanasi", "region": "Uttar Pradesh", "country": "India", "lat": 25.3176, "lng": 82.9739, "description": "One of the world's oldest continuously inhabited cities, spiritual heart of India.", "category": "heritage", "best_time_to_visit": "October to March", "entry_fee_display": "Free", "rating": 4.8, "image_url": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?q=80&w=1000&auto=format&fit=crop", "highlights": "Ganges Ghats, Kashi Vishwanath Temple, Ganga Aarti"},
    {"name": "Kerala Backwaters", "region": "Kerala", "country": "India", "lat": 9.4981, "lng": 76.3388, "description": "A network of tranquil lagoons and canals, best explored by houseboat.", "category": "nature", "best_time_to_visit": "September to March", "entry_fee_display": "Varies", "rating": 4.7, "image_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?q=80&w=1000&auto=format&fit=crop", "highlights": "Houseboat Stay, Alleppey, Kumarakom"},
]

# (origin, dest, distance, duration, mode)
ROUTES = [
    ("Mahabalipuram", "Madurai", 150, 180, "bus"),
    ("Madurai", "Rameswaram", 140, 160, "car"),
    ("Ooty", "Kodaikanal", 250, 300, "bus"),
    ("Kanyakumari", "Rameswaram", 300, 360, "train"),
    ("Pondicherry", "Mahabalipuram", 100, 120, "car"),
    ("Jaipur", "Varanasi", 650, 600, "train"),
    ("Goa", "Kerala Backwaters", 500, 540, "bus"),
]

def seed():
    app = create_app()
    with app.app_context():
        existing = {d.name: d for d in Destination.query.all()}
        added = 0
        updated = 0

        dest_map = {}
        for d in DESTINATIONS:
            if d["name"] in existing:
                dest = existing[d["name"]]
                changed = False
                for field in ("country", "image_url", "best_time_to_visit", "entry_fee_display", "rating", "highlights", "description"):
                    new_val = d.get(field)
                    if new_val is not None and getattr(dest, field, None) != new_val:
                        setattr(dest, field, new_val)
                        changed = True
                if changed:
                    updated += 1
                dest_map[d["name"]] = dest
                continue
            dest = Destination(**d)
            db.session.add(dest)
            dest_map[d["name"]] = dest
            existing[d["name"]] = dest
            added += 1
        db.session.flush()

        existing_routes = {(r.origin_id, r.dest_id) for r in Route.query.all()}
        route_count = 0
        for origin, dest, dist, dur, mode in ROUTES:
            if origin in dest_map and dest in dest_map:
                o_id = dest_map[origin].id
                d_id = dest_map[dest].id
                if (o_id, d_id) not in existing_routes:
                    route = Route(
                        origin_id=o_id,
                        dest_id=d_id,
                        distance_km=dist,
                        est_duration_min=dur,
                        mode=TravelMode(mode),
                    )
                    db.session.add(route)
                    route_count += 1

        db.session.commit()
        print(f"Seeded {added} new and updated {updated} destinations, added {route_count} routes ({len(existing)} total destinations in database).")


if __name__ == "__main__":
    seed()

