"""
Defines the FlightData class for storing flight deal information.
"""

class FlightData:
    """
    Represents a flight deal with relevant travel details.
    
    Attributes:
        price (float): The price of the flight.
        origin_city (str): Name of the departure city.
        origin_airport (str): IATA code of the departure airport.
        destination_city (str): Name of the arrival city.
        destination_airport (str): IATA code of the arrival airport.
        departure_date (str): Outbound departure date (YYYY-MM-DD).
        return_date (str): Return date (YYYY-MM-DD).
    """

    def __init__(
        self,
        price,
        origin_city,
        origin_airport,
        destination_city,
        destination_airport,
        departure_date,
        return_date
    ):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.return_date = return_date
