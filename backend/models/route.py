import enum
from extensions import db


class TravelMode(enum.Enum):
    bus = "bus"
    train = "train"
    car = "car"
    walk = "walk"


class Route(db.Model):
    __tablename__ = "routes"

    id = db.Column(db.Integer, primary_key=True)
    origin_id = db.Column(db.Integer, db.ForeignKey("destinations.id"), nullable=False)
    dest_id = db.Column(db.Integer, db.ForeignKey("destinations.id"), nullable=False)
    distance_km = db.Column(db.Float, nullable=False)
    est_duration_min = db.Column(db.Integer, nullable=False)
    mode = db.Column(db.Enum(TravelMode), nullable=False)

    origin = db.relationship(
        "Destination", foreign_keys=[origin_id], backref="routes_from"
    )
    destination = db.relationship(
        "Destination", foreign_keys=[dest_id], backref="routes_to"
    )

    def __repr__(self):
        return f"<Route {self.origin.name} -> {self.destination.name} ({self.mode.value})>"
