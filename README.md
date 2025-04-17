# ✈️ Flight Deal Finder Web App

A full-stack Flask web application that allows users to search for round-trip flight deals and logs each search to a persistent SQLite database. This project is a complete transformation of my original CLI-based [Flight Deal Finder](https://github.com/Cyber-Security-Tech/flight-deal-finder) into a modern, interactive web experience.

---

## 🌐 Live Demo

🔗 [Try the Live Web App](https://flight-deal-finder-web.onrender.com)

No sign-in required — just search for flights, view results, and browse the search history.

---

## ✅ Features

- Flask-powered web interface
- Amadeus API integration for real-time flight data
- DEMO mode for showcasing without API keys
- SQLite-backed search history with persistent logs
- `/history` route with styled table of all past searches
- Email alerts when real flight deals are found (if DEMO mode off)
- Clean and centered UI with custom CSS
- `.env` + `.gitignore` for best practices
- Deployable on Render

---

## 🔄 From Script to Web App

| Feature       | Original Script         | Web App Upgrade                             |
|---------------|--------------------------|---------------------------------------------|
| Input         | Hardcoded                | Web form with user input                    |
| Output        | Printed to console       | Styled results rendered in-browser          |
| Storage       | None                     | SQLite database logging all searches        |
| Navigation    | None                     | `/` (home) and `/history` (logs)            |
| Access        | Local only               | Accessible online via browser               |
| Demo Mode     | ❌ No                    | ✅ Yes – easy testing without API keys       |
| Email Alerts  | ❌ No                    | ✅ Sends real emails for valid deals         |
| Styling       | ❌ None                  | ✅ Fully custom layout + polish              |

---

## 🖼️ Screenshots


- **Search Form:** `media/screenshots/search_form.png`
- **Flight Result Page:** `media/screenshots/results.PNG`
- **Search History Table:** `media/screenshots/history.PNG`
- **Email Alert Example:** `media/screenshots/email_alert.PNG`

---

## 📂 Project Structure

```
flight-deal-finder-web/
│
├── run.py                     # Entry point using app factory
├── requirements.txt
├── .env.example               # Env template
├── .gitignore
│
├── app/
│   ├── __init__.py            # App factory setup
│   ├── routes.py              # Flask routes
│   ├── flight_search.py       # Amadeus API integration
│   ├── flight_data.py         # FlightData model
│   ├── search_log.py          # SQLite interaction
│   ├── notification_manager.py# Email sending logic
│   ├── templates/
│   │   ├── index.html
│   │   ├── results.html
│   │   └── history.html
│   └── static/
│       └── style.css
```

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/Cyber-Security-Tech/flight-deal-finder-web.git
cd flight-deal-finder-web

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```

Create a `.env` file based on `.env.example`:

```
AMADEUS_CLIENT_ID=your_key
AMADEUS_CLIENT_SECRET=your_secret
MY_EMAIL=your_email@gmail.com
MY_EMAIL_PASSWORD=your_gmail_app_password
```

Then run it:

```bash
python run.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Demo Mode

Don’t have API credentials? No problem. The app supports a fallback demo mode.

In `routes.py`, make sure:

```python
DEMO_MODE = True
```

You’ll get a mock flight deal without needing an API key or SMTP setup.

---

## 📜 Search History

Each user search (origin, destination, max price, timestamp) is automatically saved to a local `SQLite` database. View it at:

```
/history
```

---

## 📧 Email Alerts

When DEMO mode is off, real flight results will trigger an automated email with:

- Departure + arrival cities and airport codes
- Price, dates, and round-trip details

This is sent using `smtplib` and Gmail App Passwords securely from your `.env`.

---

## 💡 What I Learned

- Flask routing, Jinja templating, and app factory pattern
- Safe and secure `.env` usage for API + email credentials
- Integrating Amadeus API into a production-ready workflow
- Logging + querying with `sqlite3`
- Styling frontends and writing clean backend logic
- How to deploy and debug Flask apps on Render

---

## 🔒 Tech Stack

- Python 3
- Flask
- SQLite
- HTML/CSS + Jinja Templates
- Amadeus Flight Offers API
- Gmail SMTP (smtplib)
- dotenv

---

## 🚧 Future Improvements

- Deploy to custom domain with HTTPS
- User accounts and authentication
- Export search history to CSV
- Email multiple recipients or a test-mode inbox
- Daily scheduled scans for saved routes