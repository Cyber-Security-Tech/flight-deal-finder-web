"""
Handles flight search functionality using the Amadeus API.
"""

import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from amadeus import Client, ResponseError

from .flight_data import FlightData

load_dotenv()


class FlightSearch:
    """
    Provides flight search capabilities using Amadeus API.
    """

    def __init__(self):
        # Initialize Amadeus API client with credentials from .env
        self.amadeus = Client(
            client_id=os.getenv("AMADEUS_CLIENT_ID"),
            client_secret=os.getenv("AMADEUS_CLIENT_SECRET")
        )

    def search_flights(self, origin_city, destination_city, max_price):
        """
        Searches for round-trip flight offers between two cities within a given price limit.

        Args:
            origin_city (str): IATA code of the origin city.
            destination_city (str): IATA code of the destination city.
            max_price (float): Maximum price user is willing to pay.

        Returns:
            FlightData | None: A FlightData object if a suitable offer is found, otherwise None.
        """
        date_from = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        date_to = (datetime.now() + timedelta(days=180)).strftime('%Y-%m-%d')
        return_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')

        try:
            # Search for the cheapest available flight offer
            response = self.amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin_city,
                destinationLocationCode=destination_city,
                departureDate=date_from,
                returnDate=return_date,
                adults=1,
                max=1
            )

            if not response.data:
                return None

            offer = response.data[0]
            price = float(offer["price"]["total"])

            # Return FlightData if the price is within the allowed budget
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
            # Log Amadeus-specific errors
            print(f"Amadeus API error: {error}")
            return None
