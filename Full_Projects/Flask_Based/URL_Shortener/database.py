import sqlite3  # ✅ Import SQLite to manage the database

DB_FILE = "urls.db"  # ✅ Define the database file name

# ✅ Connect to the database & ensure the table exists
conn = sqlite3.connect(DB_FILE, check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS url_mapping (  # ✅ Create table if it doesn't exist
    short_url TEXT PRIMARY KEY,  # ✅ Unique short URL (hash or custom alias)
    long_url TEXT NOT NULL  # ✅ Original long URL
)
''')
conn.commit()
conn.close()  # ✅ Close global connection after setup to avoid locking issues

def save_url_mapping(short_url, long_url):
    """Saves a short URL and its corresponding long URL to the database."""
    conn = sqlite3.connect(DB_FILE)  # ✅ Open a new database connection
    cursor = conn.cursor()
    cursor.execute("INSERT INTO url_mapping (short_url, long_url) VALUES (?, ?)", (short_url, long_url))  
    # ✅ Insert the short_url & long_url into the database
    conn.commit()
    conn.close()  # ✅ Always close the connection after executing

def get_original_url(short_url):
    """Retrieves the original long URL from a given short URL."""
    conn = sqlite3.connect(DB_FILE)  # ✅ Open database connection
    cursor = conn.cursor()
    cursor.execute("SELECT long_url FROM url_mapping WHERE short_url=?", (short_url,))  
    # ✅ Fetch the original URL where short_url matches
    result = cursor.fetchone()  # ✅ Fetch the first row (if exists)
    conn.close()  # ✅ Close connection

    return result[0] if result else None  # ✅ Return original URL or None if not found

def check_if_alias_exists(short_url):
    """Checks if a short URL already exists in the database."""
    conn = sqlite3.connect(DB_FILE)  # ✅ Open database connection
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM url_mapping WHERE short_url = ?", (short_url,))  
    # ✅ Check if short_url exists
    result = cursor.fetchone()
    conn.close()  # ✅ Close connection

    return result is not None  # ✅ Return True if alias exists, False otherwise