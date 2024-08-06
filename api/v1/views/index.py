#!usr/bin/python3
"""
index module for routing
"""
from api.v1.views import api_views
from flask import jsonify, Flask


@app.teardown_appcontext
def teardown(exception):
    """
    manage breakage
    """
    storage.close()


@api_views.route('/status', strict_slashes=False)
def status():
    """
    route to status
    """
    response = {"status": "ok"}
    return jsonify(response)
