from .auth import auth_bp
from .destinations import destinations_bp
from .routes_api import routes_api_bp
from .bookings import bookings_bp

__all__ = ["auth_bp", "destinations_bp", "routes_api_bp", "bookings_bp"]
