#!usr/bin/python3
"""
index module for routing
"""
from api.v1.views import api_views
from flask import Flask


app = Flask(__name__)


app.route('/status', strict_slashes=False)
def status():
    """
    route to status
    """
    return "status: ok"
