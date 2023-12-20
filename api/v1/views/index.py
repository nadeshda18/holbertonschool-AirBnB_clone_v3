from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/stats', methods=['GET'])
def stats():
    """Return the count of all objects by type"""
    types = ["Amenity", "City", "Place", "Review", "State", "User"]
    counts = {obj_type.lower(): storage.count(obj_type) for obj_type in types}
    return jsonify(counts)
