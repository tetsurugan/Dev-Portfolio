import hashlib  # ✅ Import hashlib for SHA-256 hashing
import random
import string

def generate_hash(long_url, length=6):
    """Generates a short unique hash for a given long URL."""
    
    # ✅ Create a SHA-256 hash object from the long URL
    hash_object = hashlib.sha256(long_url.encode())  
    hash_digest = hash_object.hexdigest()  # ✅ Convert to hexadecimal format
    
    # ✅ Trim the hash to the required length (default 6 characters)
    short_hash = hash_digest[:length]  
    
    return short_hash  # ✅ Return the shortened hash as the URL key