import os
import logging
import requests
from datetime import datetime, date
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models.booking import Booking, BookingStatus
from models.route import Route

logger = logging.getLogger(__name__)

bookings_bp = Blueprint("bookings", __name__)

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "")


@bookings_bp.route("/api/bookings", methods=["POST"])
@jwt_required()
def create_booking():
    try:
        user_id = int(get_jwt_identity())
        data = request.get_json()
        route_id = data.get("route_id")
        travel_date_str = data.get("travel_date")

        if not all([route_id, travel_date_str]):
            return jsonify({"error": "route_id and travel_date are required"}), 400

        route = Route.query.get(route_id)
        if not route:
            return jsonify({"error": "Route not found"}), 404

        try:
            travel_date = datetime.strptime(travel_date_str, "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        if travel_date < date.today():
            return jsonify({"error": "Travel date cannot be in the past"}), 400

        booking = Booking(
            user_id=user_id,
            route_id=route_id,
            travel_date=travel_date,
            status=BookingStatus.pending,
        )
        db.session.add(booking)
        db.session.commit()

        if N8N_WEBHOOK_URL:
            try:
                requests.post(
                    N8N_WEBHOOK_URL,
                    json={
                        "event": "booking_created",
                        "booking_id": booking.id,
                        "user_id": user_id,
                        "route_id": route_id,
                        "travel_date": travel_date_str,
                    },
                    timeout=5,
                )
            except Exception:
                logger.warning("n8n webhook failed for booking %s", booking.id, exc_info=True)

        return jsonify({"message": "Booking created", "booking_id": booking.id}), 201
    except Exception:
        db.session.rollback()
        logger.exception("Failed to create booking")
        return jsonify({"error": "Internal server error"}), 500


@bookings_bp.route("/api/bookings", methods=["GET"])
@jwt_required()
def list_bookings():
    try:
        user_id = int(get_jwt_identity())
        bookings = Booking.query.filter_by(user_id=user_id).all()
        return jsonify(
            [
                {
                    "id": b.id,
                    "route_id": b.route_id,
                    "origin": b.route.origin.name,
                    "destination": b.route.destination.name,
                    "travel_date": b.travel_date.isoformat(),
                    "status": b.status.value,
                }
                for b in bookings
            ]
        ), 200
    except Exception:
        logger.exception("Failed to list bookings")
        return jsonify({"error": "Internal server error"}), 500


@bookings_bp.route("/api/bookings/<int:booking_id>", methods=["PATCH"])
@jwt_required()
def update_booking(booking_id):
    try:
        user_id = int(get_jwt_identity())
        booking = Booking.query.get(booking_id)

        if not booking:
            return jsonify({"error": "Booking not found"}), 404
        if booking.user_id != user_id:
            return jsonify({"error": "Unauthorized"}), 403

        data = request.get_json()
        new_status = data.get("status")

        if not new_status:
            return jsonify({"error": "status field is required"}), 400

        try:
            status_enum = BookingStatus(new_status)
        except ValueError:
            return jsonify({"error": f"Invalid status. Must be: pending, confirmed, cancelled"}), 400

        booking.status = status_enum
        db.session.commit()

        return jsonify({"message": "Booking updated", "status": booking.status.value}), 200
    except Exception:
        db.session.rollback()
        logger.exception("Failed to update booking %s", booking_id)
        return jsonify({"error": "Internal server error"}), 500


@bookings_bp.route("/api/bookings/<int:booking_id>", methods=["DELETE"])
@jwt_required()
def delete_booking(booking_id):
    try:
        user_id = int(get_jwt_identity())
        booking = Booking.query.get(booking_id)

        if not booking:
            return jsonify({"error": "Booking not found"}), 404
        if booking.user_id != user_id:
            return jsonify({"error": "Unauthorized"}), 403

        db.session.delete(booking)
        db.session.commit()

        return jsonify({"message": "Booking deleted"}), 200
    except Exception:
        db.session.rollback()
        logger.exception("Failed to delete booking %s", booking_id)
        return jsonify({"error": "Internal server error"}), 500
