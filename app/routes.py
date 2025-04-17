"""
Defines application routes for home and search history.
Handles flight search requests, mock/demo mode logic, and email notifications.
"""

from flask import Blueprint, render_template, request
from .flight_search import FlightSearch
from .flight_data import FlightData
from .search_log import log_search, get_all_searches
from .notification_manager import NotificationManager

main = Blueprint("main", __name__)

# Toggle demo mode: Set to True to use static/mock flight data for testing
DEMO_MODE = True

# Initialize helper components
flight_search = FlightSearch()
notifier = NotificationManager()


@main.route("/", methods=["GET", "POST"])
def home():
    """
    Handles the main flight search form.

    On GET: Displays the search form.
    On POST: Logs the search, performs live or mock search,
             sends notification if applicable, and renders results.
    """
    if request.method == "POST":
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        max_price = float(request.form.get("max_price"))

        # Log the search to the database
        log_search(origin, destination, max_price)

        # Use mock data if demo mode is enabled
        if DEMO_MODE:
            mock_flight = FlightData(
                price=199,
                origin_city=origin,
                origin_airport=origin,
                destination_city=destination,
                destination_airport=destination,
                departure_date="2025-06-01",
                return_date="2025-06-08"
            )
            return render_template("results.html", flight=mock_flight)
        else:
            flight = flight_search.search_flights(origin, destination, max_price)
            if flight:
                notifier.send_email(flight)
            return render_template("results.html", flight=flight)

    return render_template("index.html")


@main.route("/history")
def history():
    """
    Displays a list of all past flight searches stored in the database.
    """
    all_searches = get_all_searches()
    return render_template("history.html", searches=all_searches)
