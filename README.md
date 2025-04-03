# ✈️ Flight Deal Finder Web App

A full-stack Flask web application that allows users to search for round-trip flight deals and logs each search to a persistent SQLite database. Built as a major upgrade to the original Python-based script version by transforming it into a professional, interactive web app.

---

## 🚀 What This Project Includes

- ✅ Flask-powered web interface
- ✅ Amadeus API integration for real-time flight data
- ✅ Demo mode fallback (no API key needed)
- ✅ Logs user searches to a local SQLite database
- ✅ `/history` page to view all previous searches
- ✅ Clean and centered UI with custom styling
- ✅ `.env` and `.gitignore` best practices
- ✅ Push-ready for GitHub with clear commits and structure

---

## 🧠 From Script to Web App: How I Improved It

This project began as a simple Python script that pulled flight data using the Amadeus API and printed results to the console. Here’s how I transformed it into a full web application:

| Feature | Original Script | Web App Upgrade |
|--------|------------------|-----------------|
| Input | Hardcoded | Web form with user input |
| Output | Printed to console | Beautifully styled results in browser |
| Storage | None | SQLite database logs all searches |
| Navigation | None | `/` for search, `/history` for search logs |
| Access | Local CLI only | Browser-accessible, deployable |
| Demo Mode | No | ✅ Yes — no keys needed |
| Styling | None | Custom CSS with layout polish |

---

## 📂 Project Structure

```
flight-deal-finder-web/
│
├── app.py                      # Flask entry point with all routes
├── flight_search.py            # Logic for Amadeus API calls
├── flight_data.py              # FlightData model
├── search_log.py               # SQLite DB logic (init, log, fetch)
│
├── templates/
│   ├── index.html              # Homepage with search form
│   ├── results.html            # Shows a single search result
│   └── history.html            # Table of all past user searches
│
├── static/
│   └── style.css               # Custom CSS for UI styling
│
├── .env.example                # Template for env variables
├── requirements.txt            # All dependencies
├── .gitignore                  # Files to exclude from Git
└── README.md                   # You’re looking at it
```

---

## ⚙️ How to Run It Locally

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/flight-deal-finder-web.git
cd flight-deal-finder-web
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your `.env`

Use `.env.example` to create your `.env` file:

```env
AMADEUS_CLIENT_ID=your_key_here
AMADEUS_CLIENT_SECRET=your_secret_here
```

Set `DEMO_MODE = True` in `app.py` to test without an API key.

### 5. Run the App

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Demo Mode Fallback

If you don’t have API keys, just leave the `.env` empty and make sure:

```python
DEMO_MODE = True
```

Your browser will still show a fake but realistic flight result like this:

```
From: IAD (IAD)
To: CDG (CDG)
Price: $199
Departure: 2025-06-01
Return: 2025-06-08
```

---

## 📜 Search History

All searches (origin, destination, max price, timestamp) are logged in a local SQLite database and viewable at:

```
/history
```

The table is centered, styled, and updated with every new submission.

---

## 🧠 What I Learned

- Flask routing, templates, and server-side rendering
- How to persist data with SQLite and `sqlite3`
- Real-world API usage and fallback design patterns
- Clean architecture, file structure, and GitHub commits
- Frontend/backend coordination + UI/UX polish

---

## 🔒 Tech Used

- Python 3
- Flask
- SQLite3
- Amadeus Flight API
- HTML/CSS (Jinja templates)
- `dotenv` for secret management

---

## 💬 Next Steps (Optional)

- Email alert system
- Scheduled background job (daily check)
- Deployment to Render
- User authentication for saved alerts

---

