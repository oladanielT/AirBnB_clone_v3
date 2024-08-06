#!/usr/bin/python3
"""
index module
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def view_status():
    """
    route to status
    """
    response = {
        "status": "ok"
    }
    return jsonify(response)
