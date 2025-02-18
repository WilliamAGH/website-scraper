from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Configure database with SQLite fallback
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///dev.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize extensions
db = SQLAlchemy(app)

# Root endpoint
@app.route('/')
def index():
    """Root endpoint that provides API information."""
    return jsonify({
        "name": "mini-api-v2",
        "version": "0.1.0",
        "description": "A strongly-typed Python API server",
        "endpoints": {
            "rest": "/api",
            "trpc": "/trpc",
            "graphql": "/graphql",
            "health": "/api/health"
        }
    })

# Import routes
from api.routes.rest import health
app.register_blueprint(health.router, url_prefix='/api')

with app.app_context():
    db.create_all()