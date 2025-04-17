"""
Application factory for initializing the Flask app.
Handles configuration, database initialization, and blueprint registration.
"""

import os
from flask import Flask
from dotenv import load_dotenv

from .search_log import initialize_db
from .routes import main as main_blueprint


def create_app():
    # Load environment variables from .env file
    load_dotenv()

    # Create the Flask application instance
    app = Flask(__name__)

    # Initialize the SQLite database (create table if not exists)
    initialize_db()

    # Register application routes via blueprint
    app.register_blueprint(main_blueprint)

    return app
