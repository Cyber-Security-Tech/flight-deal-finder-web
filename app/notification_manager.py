"""
Handles email notifications for flight deals using SMTP.
"""

import os
import smtplib
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    """
    Sends email alerts when a qualifying flight deal is found.

    Attributes:
        email (str): Sender's email address (from environment variable).
        password (str): Sender's email password or app-specific password.
    """

    def __init__(self):
        self.email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_EMAIL_PASSWORD")

    def send_email(self, flight):
        """
        Sends an email containing flight deal details.

        Args:
            flight (FlightData): An instance containing flight information.
        """
        subject = f"Cheap flight alert: ${flight.price} from {flight.origin_airport} to {flight.destination_airport}"
        body = (
            f"A cheap flight was found:\n\n"
            f"From: {flight.origin_city} ({flight.origin_airport})\n"
            f"To: {flight.destination_city} ({flight.destination_airport})\n"
            f"Price: ${flight.price}\n"
            f"Departure: {flight.departure_date}\n"
            f"Return: {flight.return_date}"
        )

        message = f"Subject: {subject}\n\n{body}"

        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.email, password=self.password)
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=self.email,
                    msg=message.encode("utf-8")
                )
                print("Email sent successfully.")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")
