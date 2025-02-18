from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import text
from dotenv import load_dotenv
import os
import logging
from api.utils.logger import setup_logger
from urllib.parse import urlparse

# Load environment variables
load_dotenv()

# Initialize logger
logger = setup_logger(__name__)

# Get port from environment variables with fallback logic
def get_api_port():
    api_port = os.environ.get("API_PORT")
    if api_port:
        return int(api_port)

    api_url = os.environ.get("API_URL")
    if api_url:
        try:
            return int(urlparse(api_url).port or 5000)
        except (ValueError, TypeError):
            pass

    return 5000

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Get the API and APP URLs from environment
    api_url = os.environ.get("API_URL", "http://localhost:5000")
    app_url = os.environ.get("APP_URL", "http://localhost:3000")

    # Enable CORS for development
    CORS(app, resources={
        r"/api/*": {
            "origins": [app_url],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    app.secret_key = os.environ.get("SESSION_SECRET")

    # Configure the database
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
    }

    # Initialize extensions
    db.init_app(app)

    with app.app_context():
        # Import routes
        from api.routes.rest import register_rest_routes
        from api.routes.graphql import register_graphql_routes
        from api.routes.trpc import register_trpc_routes

        # Register routes
        register_rest_routes(app)
        register_graphql_routes(app)
        register_trpc_routes(app)

        # Create database tables
        db.create_all()

        @app.route("/")
        def index():
            """Root endpoint that lists available API endpoints."""
            return jsonify({
                "message": "Welcome to mini-api-v2",
                "version": "0.1.0",
                "endpoints": {
                    "rest": {
                        "base": "/api/v1",
                        "health": "/api/health",
                        "auth": "/api/v1/auth/*",
                        "users": "/api/v1/users/*",
                        "posts": "/api/v1/posts/*"
                    },
                    "graphql": "/graphql",
                    "trpc": "/trpc/*"
                }
            })

        @app.route("/api/health")
        def health_check():
            """Health check endpoint."""
            try:
                db.session.execute(text("SELECT 1"))
                return jsonify({
                    "status": "healthy",
                    "database": "connected",
                    "api_url": os.environ.get("API_URL"),
                    "app_url": os.environ.get("APP_URL")
                })
            except Exception as e:
                logger.error(f"Health check failed: {str(e)}")
                return jsonify({"status": "unhealthy", "error": str(e)}), 500

        return app

app = create_app()

if __name__ == "__main__":
    port = get_api_port()
    logger.info(f"Starting server on port {port}")
    app.run(host="0.0.0.0", port=port, debug=True)