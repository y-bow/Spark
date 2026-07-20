import logging
from flask import Blueprint, jsonify, request
from models.destination import Destination

logger = logging.getLogger(__name__)

destinations_bp = Blueprint("destinations", __name__)


@destinations_bp.route("/api/destinations", methods=["GET"])
def list_destinations():
    try:
        query = Destination.query

        country = request.args.get("country", "").strip()
        region = request.args.get("region", "").strip()

        if country:
            query = query.filter(Destination.country.ilike(f"%{country}%"))
        if region:
            query = query.filter(Destination.region.ilike(f"%{region}%"))

        destinations = query.all()
        return jsonify(
            [
                {
                    "id": d.id,
                    "name": d.name,
                    "region": d.region,
                    "country": d.country,
                    "lat": d.lat,
                    "lng": d.lng,
                    "description": d.description,
                    "category": d.category,
                    "best_time_to_visit": d.best_time_to_visit,
                    "entry_fee_display": d.entry_fee_display,
                    "rating": d.rating,
                    "image_url": d.image_url,
                    "highlights": d.highlights,
                }
                for d in destinations
            ]
        ), 200
    except Exception:
        logger.exception("Failed to list destinations")
        return jsonify({"error": "Internal server error"}), 500


@destinations_bp.route("/api/destinations/<int:dest_id>", methods=["GET"])
def get_destination(dest_id):
    try:
        d = Destination.query.get(dest_id)
        if not d:
            return jsonify({"error": "Destination not found"}), 404
        return jsonify(
            {
                "id": d.id,
                "name": d.name,
                "region": d.region,
                "country": d.country,
                "lat": d.lat,
                "lng": d.lng,
                "description": d.description,
                "category": d.category,
                "best_time_to_visit": d.best_time_to_visit,
                "entry_fee_display": d.entry_fee_display,
                "rating": d.rating,
                "image_url": d.image_url,
                "highlights": d.highlights,
            }
        ), 200
    except Exception:
        logger.exception("Failed to get destination %s", dest_id)
        return jsonify({"error": "Internal server error"}), 500
