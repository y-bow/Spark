from app import create_app
from extensions import db
from models.user import User, Role
from models.destination import Destination
from models.route import Route, TravelMode
from models.booking import Booking, BookingStatus
from datetime import date, timedelta
import random

def seed_bookings():
    app = create_app()
    with app.app_context():
        # Ensure we have a user
        user = User.query.first()
        if not user:
            # Create a dummy user if none exists
            user = User(name="Demo User", email="demo@example.com", password_hash="dummy_hash", role=Role.visitor)
            db.session.add(user)
            db.session.commit()

        # Ensure we have destinations and routes
        destinations = Destination.query.all()
        if not destinations:
            print("No destinations found. Please run seed.py first.")
            return

        routes = Route.query.all()
        if not routes:
            print("No routes found. Please run seed.py first.")
            return

        # Clear existing bookings to avoid duplicates if re-running
        Booking.query.delete()

        statuses = [BookingStatus.pending, BookingStatus.confirmed, BookingStatus.cancelled]
        
        print(f"Seeding bookings for user: {user.name}")

        for _ in range(10):
            route = random.choice(routes)
            booking = Booking(
                user_id=user.id,
                route_id=route.id,
                travel_date=date.today() + timedelta(days=random.randint(1, 365)),
                status=random.choice(statuses)
            )
            db.session.add(booking)
        
        db.session.commit()
        print("Successfully seeded 10 sample bookings.")

if __name__ == "__main__":
    seed_bookings()
