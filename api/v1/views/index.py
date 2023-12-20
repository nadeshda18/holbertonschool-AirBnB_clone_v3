#!/usr/bin/python3
"""index module
This module contains the routes for the status
and stats endpoint"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


@app_views.route('/status', methods=['GET'])
def status():
    """Return server status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """Retrieve the number of each objects by type"""
    return jsonify({
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    })
