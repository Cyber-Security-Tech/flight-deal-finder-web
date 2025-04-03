from flask import Flask, render_template, request
from flight_search import FlightSearch
from flight_data import FlightData
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
flight_search = FlightSearch()

# 🔧 Toggle demo mode ON to use mock data without API keys
DEMO_MODE = True

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        max_price = float(request.form.get("max_price"))

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

if __name__ == "__main__":
    app.run(debug=True)
