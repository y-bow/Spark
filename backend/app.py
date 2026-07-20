import os
import logging
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from extensions import db
from routes import auth_bp, destinations_bp, routes_api_bp, bookings_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    logging.basicConfig(level=logging.INFO)
    app.logger.setLevel(logging.INFO)

    db.init_app(app)
    JWTManager(app)

    allowed = [
        app.config["FRONTEND_URL"],
        "http://localhost:5500",
        "http://localhost:3000",
        "http://127.0.0.1:5500",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8080",
        "http://localhost:8080",
        "https://travelpulse-app.netlify.app",
        "null",
    ]
    CORS(app, origins=allowed)

    app.register_blueprint(auth_bp)
    app.register_blueprint(destinations_bp)
    app.register_blueprint(routes_api_bp)
    app.register_blueprint(bookings_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
