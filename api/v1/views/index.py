#!/usr/bin/python3
"""
index module
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def view_status():
    """
    route to status
    """
    response = {
        "status": "ok"
    }
    return jsonify(response)


@app_views.route('/stats', strict_slashes=False)
def view_stat():
    """
    route to stats
    """
    stats = {
        "amenities": storage.count('Amenity'),
        "cities": storage.count('City'),
        "places": storage.count('Place'),
        "reviews": storage.count('Review'),
        "states": storage.count('State'),
        "users": storage.count('User')
    }
    return jsonify(stats)
