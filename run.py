"""
Entry point for the Flask application.
Initializes the app using the application factory pattern.
"""

from app import create_app

# Create the Flask app instance
app = create_app()

if __name__ == "__main__":
    # Enable debug mode for development
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

