"""
Entry point for the Flask application.
Initializes the app using the application factory pattern.
"""

from app import create_app

# Create the Flask app instance
app = create_app()

if __name__ == "__main__":
    # Enable debug mode for development
    app.run(debug=True)
