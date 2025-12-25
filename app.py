import os
import re
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from pymongo import MongoClient
from functools import wraps

app = Flask(__name__)

# --- 1. SECURITY CONFIGURATION ---

# A. Strict CORS: Only allow your Frontend (Next.js) to talk to this API
# In production, change this to your actual domain (e.g., https://threatsys.co.in)
ALLOWED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]
CORS(app, resources={r"/api/*": {"origins": ALLOWED_ORIGINS}})

# B. Admin Secret Key (In production, use os.getenv('ADMIN_SECRET'))
# This ensures that even if someone finds the API URL, they can't edit data without this key.
ADMIN_SECRET_KEY = "threatsys_super_secure_key_2025"

# --- 2. DATABASE CONNECTION ---
client = MongoClient("mongodb+srv://maharanapratik600_db_user:iZpG6TsJjNkH0cfd@threatsyscluster.lgp7wyz.mongodb.net/?retryWrites=true&w=majority&appName=ThreatsysCluster")
db = client["threatsys_cms"]
pages_collection = db["pages"]
cert_collection = db["certificates"]

# --- 3. SECURITY MIDDLEWARE ---

def require_admin_key(f):
    """Decorator to require x-admin-key header for admin routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if the custom header matches our secret
        apiKey = request.headers.get('x-admin-key')
        if apiKey != ADMIN_SECRET_KEY:
            return jsonify({"error": "Unauthorized: Invalid Admin Key"}), 401
        return f(*args, **kwargs)
    return decorated_function

def sanitize_regex(query):
    """Escapes regex special characters to prevent ReDoS attacks."""
    return re.escape(query)

@app.after_request
def add_security_headers(response):
    """Add standard security headers to every response."""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

# --- 4. PUBLIC ROUTES (Safe for everyone) ---

@app.route('/api/content/<slug>', methods=['GET'])
def get_page(slug):
    # Sanitize slug to ensure it's just alphanumeric and dashes
    if not re.match(r'^[a-z0-9-]+$', slug):
        return jsonify({"error": "Invalid slug format"}), 400
        
    page = pages_collection.find_one({"slug": slug}, {"_id": 0})
    if page:
        return jsonify(page), 200
    return jsonify({"error": "Page not found"}), 404

@app.route('/api/blog/post/<post_slug>', methods=['GET'])
def get_blog_post(post_slug):
    if not re.match(r'^[a-z0-9-]+$', post_slug):
        return jsonify({"error": "Invalid slug format"}), 400

    blog_page = pages_collection.find_one({"slug": "blog"})
    if blog_page and "sections" in blog_page and "posts" in blog_page["sections"]:
        posts = blog_page["sections"]["posts"]
        for post in posts:
            if post.get("slug") == post_slug:
                return jsonify(post), 200
    return jsonify({"error": "Post not found"}), 404

@app.route('/api/pages', methods=['GET'])
def get_all_pages():
    pages = list(pages_collection.find({}, {"_id": 0, "slug": 1, "title": 1}))
    return jsonify(pages), 200

@app.route('/api/certificates/search', methods=['GET'])
def search_certificates():
    query = request.args.get('q', '')
    if not query or len(query) > 50: # Limit length to prevent buffer overflows/slow regex
        return jsonify([])

    # SECURITY: Escape the query so users can't inject regex commands
    safe_query = sanitize_regex(query)
    
    regex_query = {"$regex": safe_query, "$options": "i"}
    
    results = list(cert_collection.find({
        "$or": [
            {"company_name": regex_query},
            {"cert_id": regex_query},
            {"address": regex_query}
        ]
    }, {"_id": 0}))
    
    return jsonify(results)


# --- 5. PROTECTED ADMIN ROUTES (Require Key) ---

@app.route('/api/admin/update/<slug>', methods=['PUT'])
@require_admin_key  # <--- PROTECTED
def update_page(slug):
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    pages_collection.update_one(
        {"slug": slug},
        {"$set": {
            "title": data.get('title'),
            "sections": data.get('sections')
        }}
    )
    return jsonify({"message": "Updated successfully"}), 200

@app.route('/api/admin/certificates', methods=['GET', 'POST', 'PUT', 'DELETE'])
@require_admin_key  # <--- PROTECTED
def manage_certificates():
    # GET is okay for admins, but we still protect it to hide bulk data
    if request.method == 'GET':
        return jsonify(list(cert_collection.find({}, {"_id": 0})))
    
    if request.method == 'POST':
        data = request.json
        # Basic validation
        if not data.get('cert_id') or not data.get('company_name'):
             return jsonify({"error": "Missing required fields"}), 400
             
        cert_collection.insert_one(data)
        return jsonify({"msg": "Added"}), 201

    if request.method == 'PUT':
        data = request.json
        cert_id = request.args.get('id')
        cert_collection.update_one({"cert_id": cert_id}, {"$set": data})
        return jsonify({"msg": "Updated"}), 200

    if request.method == 'DELETE':
        cert_id = request.args.get('id')
        cert_collection.delete_one({"cert_id": cert_id})
        return jsonify({"msg": "Deleted"}), 200

# --- 6. RUN SERVER ---
if __name__ == '__main__':
    # SECURITY: Turn DEBUG OFF for production-like behavior
    # Use environment variable for port
    app.run(debug=False, port=5000, host='0.0.0.0')