from extensions import db


class Destination(db.Model):
    __tablename__ = "destinations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    region = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(120), nullable=True)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(80), nullable=True)
    best_time_to_visit = db.Column(db.String(120), nullable=True)
    entry_fee_display = db.Column(db.String(50), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    image_url = db.Column(db.String(500), nullable=True)
    highlights = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"<Destination {self.name} ({self.region})>"
