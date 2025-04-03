from flask import Flask, render_template, request
from flight_search import FlightSearch
from flight_data import FlightData
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
flight_search = FlightSearch()

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        max_price = float(request.form.get("max_price"))

        flight = flight_search.search_flights(origin, destination, max_price)
        return render_template("results.html", flight=flight)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
