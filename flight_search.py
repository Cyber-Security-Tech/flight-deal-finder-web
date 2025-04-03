import os
from amadeus import Client, ResponseError
from dotenv import load_dotenv
from flight_data import FlightData
from datetime import datetime, timedelta

load_dotenv()

amadeus = Client(
    client_id=os.getenv("AMADEUS_CLIENT_ID"),
    client_secret=os.getenv("AMADEUS_CLIENT_SECRET")
)

class FlightSearch:
    def search_flights(self, origin_city, destination_city, max_price):
        date_from = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        date_to = (datetime.now() + timedelta(days=180)).strftime('%Y-%m-%d')

        try:
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin_city,
                destinationLocationCode=destination_city,
                departureDate=date_from,
                returnDate=(datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'),
                adults=1,
                max=1
            )

            if not response.data:
                return None

            offer = response.data[0]
            price = float(offer["price"]["total"])

            if price <= max_price:
                itinerary = offer["itineraries"][0]["segments"][0]
                return FlightData(
                    price=price,
                    origin_city=origin_city,
                    origin_airport=itinerary["departure"]["iataCode"],
                    destination_city=destination_city,
                    destination_airport=itinerary["arrival"]["iataCode"],
                    departure_date=itinerary["departure"]["at"].split("T")[0],
                    return_date=offer["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")[0]
                )
        except ResponseError as error:
            print(f"Amadeus API error: {error}")
            return None
