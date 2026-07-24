from flask import Blueprint, jsonify
from extensions import db
from models.booking import Booking
from models.destination import Destination
from models.route import Route

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/api/analytics/export')
def export_analytics():
    try:
        # Safeguard: if there are zero bookings, return an empty array
        if not Booking.query.first():
            return jsonify([]), 200

        results = db.session.query(
            Booking.id, Booking.travel_date, Booking.status,
            Destination.name, Destination.region, Destination.category,
            Destination.country, Destination.lat, Destination.lng,
            Route.mode, Route.distance_km
        ).join(Route, Booking.route_id == Route.id)\
         .join(Destination, Route.dest_id == Destination.id).all()

        data = [{
            "booking_id": r[0], 
            "travel_date": str(r[1]), 
            "status": r[2].value if hasattr(r[2], 'value') else str(r[2]),
            "destination": r[3], 
            "region": r[4], 
            "category": r[5],
            "country": r[6], 
            "lat": r[7], 
            "lng": r[8],
            "mode": r[9].value if hasattr(r[9], 'value') else str(r[9]), 
            "distance_km": r[10]
        } for r in results]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": "Could not export analytics data"}), 500
