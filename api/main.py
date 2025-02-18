from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os
import logging
from api.utils.logger import setup_logger

# Load environment variables
load_dotenv()

# Initialize logger
logger = setup_logger(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    # Enable CORS for development
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
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
                db.session.execute("SELECT 1")
                return jsonify({"status": "healthy", "database": "connected"})
            except Exception as e:
                logger.error(f"Health check failed: {str(e)}")
                return jsonify({"status": "unhealthy", "error": str(e)}), 500

        return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)