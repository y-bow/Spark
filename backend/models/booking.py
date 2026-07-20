import enum
from extensions import db


class BookingStatus(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)
    travel_date = db.Column(db.Date, nullable=False)
    status = db.Column(
        db.Enum(BookingStatus), default=BookingStatus.pending, nullable=False
    )

    route = db.relationship("Route", backref="bookings")

    def __repr__(self):
        return f"<Booking #{self.id} status={self.status.value}>"
