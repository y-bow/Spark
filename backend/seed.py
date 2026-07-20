from app import create_app
from extensions import db
from models.destination import Destination
from models.route import Route, TravelMode

DESTINATIONS = [
    {"name": "Chennai", "region": "Coromandel", "lat": 13.0827, "lng": 80.2707, "description": "The vibrant capital of Tamil Nadu, known for its rich culture and beaches.", "category": "city", "best_time_to_visit": "November to February", "entry_fee_display": "Free", "rating": 4.2, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Marina Beach, Kapaleeshwarar Temple, San Thome Basilica"},
    {"name": "Madurai", "region": "Southern", "lat": 9.9252, "lng": 78.1198, "description": "An ancient city famed for its stunning Meenakshi Amman Temple.", "category": "heritage", "best_time_to_visit": "October to March", "entry_fee_display": "Free", "rating": 4.7, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Meenakshi Amman Temple, Thirumalai Nayakkar Mahal"},
    {"name": "Ooty", "region": "Nilgiris", "lat": 11.4102, "lng": 76.6950, "description": "A picturesque hill station surrounded by tea gardens and mountains.", "category": "hillstation", "best_time_to_visit": "April to June", "entry_fee_display": "Varies", "rating": 4.5, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Botanical Gardens, Nilgiri Mountain Railway"},
    {"name": "Coimbatore", "region": "Western", "lat": 11.0168, "lng": 76.9558, "description": "The industrial hub of Tamil Nadu, gateway to the Nilgiris.", "category": "city", "best_time_to_visit": "September to March", "entry_fee_display": "Free", "rating": 4.0, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Adiyogi Shiva Statue, Marudhamalai Temple"},
    {"name": "Kodaikanal", "region": "Palani Hills", "lat": 10.2413, "lng": 77.4863, "description": "A tranquil hill station known for its misty lakes and forests.", "category": "hillstation", "best_time_to_visit": "April to June", "entry_fee_display": "Varies", "rating": 4.6, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Kodai Lake, Pillar Rocks, Pine Forests"},
    {"name": "Rameswaram", "region": "Southern", "lat": 9.2876, "lng": 79.3129, "description": "A sacred island town and major pilgrimage destination.", "category": "pilgrimage", "best_time_to_visit": "October to March", "entry_fee_display": "Free", "rating": 4.8, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Ramanathaswamy Temple, Pamban Bridge"},
    {"name": "Kanchipuram", "region": "Coromandel", "lat": 12.8342, "lng": 79.7036, "description": "The City of Thousand Temples and famous for its silk sarees.", "category": "heritage", "best_time_to_visit": "November to February", "entry_fee_display": "Free", "rating": 4.4, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Kanchi Kamakshi Amman Temple, Silk Weaving"},
    {"name": "Pondicherry", "region": "Coromandel", "lat": 11.9416, "lng": 79.8083, "description": "A beautiful coastal town with French colonial influence.", "category": "heritage", "best_time_to_visit": "October to March", "entry_fee_display": "Free", "rating": 4.5, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "French Quarter, Promenade Beach, Auroville"},
    {"name": "Thanjavur", "region": "Cauvery Delta", "lat": 10.7870, "lng": 79.1378, "description": "A center of Chola arts and architecture with ancient temples.", "category": "heritage", "best_time_to_visit": "November to February", "entry_fee_display": "Free", "rating": 4.7, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Brihadeeswarar Temple, Maratha Palace"},
    {"name": "Mudumalai", "region": "Nilgiris", "lat": 11.5728, "lng": 76.5583, "description": "A lush wildlife sanctuary ideal for nature enthusiasts.", "category": "nature", "best_time_to_visit": "October to March", "entry_fee_display": "Varies", "rating": 4.4, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Elephant sightings, Jungle Safaris"},
    {"name": "Mahabalipuram", "region": "Coromandel", "lat": 12.6269, "lng": 80.1922, "description": "Renowned for its UNESCO-listed shore temples and rock carvings.", "category": "heritage", "best_time_to_visit": "November to February", "entry_fee_display": "₹40", "rating": 4.6, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Shore Temple, Five Rathas"},
    {"name": "Yercaud", "region": "Shevaroy Hills", "lat": 11.7786, "lng": 78.2060, "description": "A serene hill station with scenic viewpoints and lakes.", "category": "hillstation", "best_time_to_visit": "April to June", "entry_fee_display": "Free", "rating": 4.2, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Emerald Lake, Pagoda Point"},
    {"name": "Tiruchirappalli", "region": "Cauvery Delta", "lat": 10.7905, "lng": 78.7047, "description": "A historical city known for the Rock Fort and Srirangam Temple.", "category": "city", "best_time_to_visit": "November to February", "entry_fee_display": "Free", "rating": 4.1, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Rockfort Temple, Srirangam Temple"},
    {"name": "Coonoor", "region": "Nilgiris", "lat": 11.3530, "lng": 76.7968, "description": "Famous for its tea estates and the Nilgiri Mountain Railway.", "category": "hillstation", "best_time_to_visit": "October to March", "entry_fee_display": "Free", "rating": 4.5, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Tea Estates, Sim's Park"},
    {"name": "Kanyakumari", "region": "Southern", "lat": 8.0883, "lng": 77.5385, "description": "The tip of India where three seas meet, offering beautiful sunrises.", "category": "pilgrimage", "best_time_to_visit": "October to March", "entry_fee_display": "Free", "rating": 4.7, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Vivekananda Rock Memorial, Thiruvalluvar Statue"},
    {"name": "Vellore", "region": "Northern", "lat": 12.9165, "lng": 79.1325, "description": "A historical city with a famous fort and Golden Temple.", "category": "heritage", "best_time_to_visit": "November to February", "entry_fee_display": "Free", "rating": 4.0, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Vellore Fort, Golden Temple"},
    {"name": "Pollachi", "region": "Western", "lat": 10.6580, "lng": 76.9963, "description": "A lush town known for its coconut groves and scenic landscapes.", "category": "nature", "best_time_to_visit": "September to March", "entry_fee_display": "Free", "rating": 4.3, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Anamalai Tiger Reserve, Coconut Groves"},
    {"name": "Dindigul", "region": "Southern", "lat": 10.3472, "lng": 77.9649, "description": "A historical hill town known for its rock fort and delicious biryani.", "category": "heritage", "best_time_to_visit": "October to March", "entry_fee_display": "Free", "rating": 3.9, "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop", "highlights": "Dindigul Rock Fort, Biryani"},
],

ROUTES = [
    ("Chennai", "Mahabalipuram", 58, 80, "car"),
    ("Chennai", "Kanchipuram", 75, 90, "bus"),
    ("Chennai", "Pondicherry", 150, 180, "bus"),
    ("Chennai", "Coimbatore", 505, 420, "train"),
    ("Chennai", "Madurai", 462, 390, "train"),
    ("Chennai", "Ooty", 535, 480, "car"),
    ("Madurai", "Rameswaram", 170, 180, "bus"),
    ("Madurai", "Kodaikanal", 120, 180, "car"),
    ("Madurai", "Kanyakumari", 250, 300, "bus"),
    ("Madurai", "Dindigul", 70, 80, "bus"),
    ("Coimbatore", "Ooty", 86, 180, "car"),
    ("Coimbatore", "Pollachi", 55, 70, "bus"),
    ("Coimbatore", "Kodaikanal", 140, 210, "car"),
    ("Coimbatore", "Yercaud", 210, 300, "car"),
    ("Ooty", "Coonoor", 20, 30, "train"),
    ("Ooty", "Mudumalai", 36, 60, "car"),
    ("Tiruchirappalli", "Thanjavur", 57, 60, "bus"),
    ("Tiruchirappalli", "Madurai", 137, 150, "train"),
    ("Tiruchirappalli", "Ooty", 210, 300, "car"),
    ("Vellore", "Chennai", 130, 150, "bus"),
    ("Chennai", "Tiruchirappalli", 330, 300, "train"),
    ("Tiruchirappalli", "Rameswaram", 220, 240, "train"),
    ("Madurai", "Coimbatore", 210, 240, "train"),
    ("Kodaikanal", "Coonoor", 180, 270, "car"),
]


def seed():
    app = create_app()
    with app.app_context():
        if Destination.query.first():
            print("Database already seeded, skipping.")
            return

        dest_map = {}
        for d in DESTINATIONS:
            dest = Destination(**d)
            db.session.add(dest)
            dest_map[d["name"]] = dest
        db.session.flush()

        for origin, dest, dist, dur, mode in ROUTES:
            route = Route(
                origin_id=dest_map[origin].id,
                dest_id=dest_map[dest].id,
                distance_km=dist,
                est_duration_min=dur,
                mode=TravelMode(mode),
            )
            db.session.add(route)

        db.session.commit()
        print(f"Seeded {len(DESTINATIONS)} destinations and {len(ROUTES)} routes.")


if __name__ == "__main__":
    seed()
