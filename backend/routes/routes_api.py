import logging
from flask import Blueprint, request, jsonify
from models.route import Route
from models.destination import Destination

logger = logging.getLogger(__name__)

routes_api_bp = Blueprint("routes_api", __name__)


@routes_api_bp.route("/api/routes", methods=["GET"])
def list_routes():
    try:
        origin_name = request.args.get("origin")
        dest_name = request.args.get("dest")

        query = Route.query

        if origin_name:
            origin_dest = Destination.query.filter(
                Destination.name.ilike(f"%{origin_name}%")
            ).first()
            if origin_dest:
                query = query.filter_by(origin_id=origin_dest.id)

        if dest_name:
            dest_dest = Destination.query.filter(
                Destination.name.ilike(f"%{dest_name}%")
            ).first()
            if dest_dest:
                query = query.filter_by(dest_id=dest_dest.id)

        routes = query.all()
        return jsonify(
            [
                {
                    "id": r.id,
                    "origin": r.origin.name,
                    "origin_lat": r.origin.lat,
                    "origin_lng": r.origin.lng,
                    "destination": r.destination.name,
                    "dest_lat": r.destination.lat,
                    "dest_lng": r.destination.lng,
                    "distance_km": r.distance_km,
                    "est_duration_min": r.est_duration_min,
                    "mode": r.mode.value,
                }
                for r in routes
            ]
        ), 200
    except Exception:
        logger.exception("Failed to list routes")
        return jsonify({"error": "Internal server error"}), 500
