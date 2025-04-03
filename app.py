from flask import Flask, render_template, request
from flight_search import FlightSearch
from flight_data import FlightData
from search_log import initialize_db, log_search, get_all_searches
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
flight_search = FlightSearch()

# 🔧 Toggle this to enable or disable demo mode
DEMO_MODE = True

# 🔧 Initialize the database on startup
initialize_db()

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        max_price = float(request.form.get("max_price"))

        # ✅ Log search
        log_search(origin, destination, max_price)

        if DEMO_MODE:
            print("🎓 DEMO MODE ACTIVE – using mock flight data")
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
            return render_template("results.html", flight=flight)

    return render_template("index.html")

@app.route('/history')
def history():
    all_searches = get_all_searches()
    return render_template("history.html", searches=all_searches)

if __name__ == "__main__":
    app.run(debug=True)
