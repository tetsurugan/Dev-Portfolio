# Flask URL Shortener - Pseudo Code
# ----------------------------------
# This file outlines the logic for building a URL shortener in Flask.

# 1️⃣ Import necessary modules
# from flask import Flask, request, redirect, render_template
# from database_module import save_url_mapping, get_original_url, track_click
# import hashing_module  # To generate short URLs

# Initialize Flask app
# app = Flask(__name__)

# 2️⃣ Function to Shorten a URL
def shorten_url(long_url, custom_alias=None):
    """
    Takes a long URL and returns a shortened version.
    
    Parameters:
        long_url (str): The original long URL.
        custom_alias (str, optional): A custom short URL, if provided.
    
    Returns:
        str: The shortened URL or an error message if a custom alias is taken.
    """

    # ✅ If user provides a custom alias, check if it already exists
    # if custom_alias:
    #     if check_if_alias_exists(custom_alias):
    #         return "Error: Custom alias is already taken"
    #     else:
    #         short_url = custom_alias
    
    # ✅ Otherwise, generate a short hash for the URL
    # else:
    #     short_url = hashing_module.generate_hash(long_url)  # (Use Base62 or another encoding)

    # ✅ Ensure no collisions (if hash already exists, regenerate)
    # while check_if_alias_exists(short_url):
    #     short_url = hashing_module.generate_new_hash(long_url)
    
    # ✅ Save mapping (short_url → long_url) in database
    # save_url_mapping(short_url, long_url)

    # ✅ Return the generated short URL
    # return short_url

# 3️⃣ Redirect Function - When a user visits a short URL, redirect to the original
@app.route('/<short_url>')
def redirect_to_original(short_url):
    """
    Redirects user from a short URL to the original long URL.
    
    Parameters:
        short_url (str): The shortened URL key.
    
    Returns:
        Redirect: Redirects to the original long URL if found, else returns a 404.
    """

    # ✅ Retrieve the original URL from the database
    # original_url = get_original_url(short_url)

    # ✅ If the URL exists, track click and redirect
    # if original_url:
    #     track_click(short_url)  # Log the visit in database
    #     return redirect(original_url)
    
    # ✅ If the URL does not exist, return a 404 error
    # return "Error: Short URL not found", 404

# 4️⃣ Optional Features:
# - Expiration Time: If a short URL has expired, return a "410 Gone" status
# - Click Tracking: Log number of visits, timestamps, and locations
# - API Support: Allow users to shorten URLs via API requests

# Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)