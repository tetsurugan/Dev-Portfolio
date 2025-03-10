from flask import Flask, request, jsonify, redirect  # ✅ Import Flask & helper functions
from hashing import generate_hash  # ✅ Import hash generator
from database import save_url_mapping, get_original_url, check_if_alias_exists  # ✅ Import database functions

app = Flask(__name__)  # ✅ Initialize Flask app

@app.route('/shorten', methods=['POST'])  # ✅ Route to handle URL shortening
def shorten_url():
    """Handles URL shortening requests."""
    data = request.json  # ✅ Read JSON request data
    long_url = data.get('long_url')  # ✅ Extract long URL from request
    custom_alias = data.get('custom_alias')  # ✅ Check if user provided a custom alias

    if not long_url:
        return jsonify({"error": "Missing long_url"}), 400  # ✅ Return error if no URL provided

    # ✅ If user provides a custom alias, check if it's available
    if custom_alias:
        if check_if_alias_exists(custom_alias):  # ✅ Ensure alias is unique
            return jsonify({"error": "Custom alias already taken"}), 400
        short_url = custom_alias  # ✅ Use custom alias
    else:
        short_url = generate_hash(long_url)  # ✅ Generate a short hash
        while check_if_alias_exists(short_url):  # ✅ Ensure hash is unique
            short_url = generate_hash(long_url)  # ✅ Regenerate if duplicate

    # ✅ Save the short & long URL mapping to the database
    save_url_mapping(short_url, long_url)

    return jsonify({"short_url": f"http://127.0.0.1:5000/{short_url}"}), 201  # ✅ Return the shortened URL

@app.route('/')  # ✅ Root route (test message)
def home():
    return jsonify({"message": "Flask is running successfully!"})

@app.route('/<short_url>')  # ✅ Redirect route
def redirect_to_original(short_url):
    """Redirects the user to the original long URL."""
    original_url = get_original_url(short_url)  # ✅ Fetch original URL
    if original_url:
        return redirect(original_url)  # ✅ Redirect user to original URL
    return jsonify({"error": "Short URL not found"}), 404  # ✅ Return error if not found

if __name__ == "__main__":
    app.run(debug=True)  # ✅ Run the Flask app in debug mode