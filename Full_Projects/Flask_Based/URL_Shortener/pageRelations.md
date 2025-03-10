🔹 1. app.py (Main Application & API)
	•	Acts as the Flask web server and defines API routes for shortening and redirecting URLs.
	•	Handles user requests (e.g., shortens a new URL, redirects users).
	•	Calls functions from database.py to save/retrieve data.
	•	Calls generate_hash() from hashing.py to generate a short URL.

✅ How it interacts with:
	•	database.py → Calls functions to store & retrieve URLs.
	•	hashing.py → Calls the generate_hash() function to create short URLs.

     2. database.py (Database Management)
	•	Handles all database operations (saving, retrieving, and checking URL mappings).
	•	Manages an SQLite database (urls.db) to store short-long URL pairs.
	•	Ensures data persistence, meaning URLs remain stored even if you restart the app.

✅ How it interacts with:
	•	app.py → app.py calls functions from database.py to store and retrieve URL mappings.
	•	Independent → It doesn’t need hashing.py directly; it only deals with database actions.


    🔹 3. hashing.py (Short URL Generation)
	•	Creates unique short URL hashes for given long URLs.
	•	Uses SHA-256 hashing and trims it down to a shorter, fixed-length string.
	•	Ensures uniqueness by checking with database.py to avoid duplicate short links.

✅ How it interacts with:
	•	app.py → app.py calls generate_hash() to create short URLs before saving them in the database.
	•	Does NOT interact with database.py directly, it just returns a hash.

     Full Flow: How Everything Connects

Step-by-Step URL Shortening Process

1️⃣ User sends a POST request to /shorten with a long URL
	•	This request is handled by app.py (Flask server).
	•	app.py extracts the long URL from the request.

2️⃣ Flask calls generate_hash() from hashing.py
	•	The generate_hash() function creates a unique 6-character hash.

3️⃣ Flask calls check_if_alias_exists() from database.py
	•	Ensures that the generated short URL doesn’t already exist in the database.
	•	If a duplicate exists, a new hash is generated.

4️⃣ Flask calls save_url_mapping() from database.py
	•	Saves the short-long URL pair in the SQLite database.

5️⃣ Flask responds with the shortened URL (http://127.0.0.1:5000/abc123)
	•	The user now has a short URL.

    Step-by-Step URL Redirection Process

1️⃣ User visits http://127.0.0.1:5000/abc123 (the shortened URL)
	•	Flask’s redirect_to_original(short_url) function in app.py is triggered.

2️⃣ Flask calls get_original_url(short_url) from database.py
	•	Searches the database for the original long URL.

3️⃣ If found, Flask redirects the user to the original URL
	•	If abc123 exists in the database, Flask redirects the user.
	•	If not found, it returns a 404 error.