#/usr/bin/python3
"""
Create a new view for State objects that handles all default RESTFul API actions
"""
from models import storage
from api.v1.views import app_views
from models.state import State
from flask import Flask, jsonify, abort


@app_views.route('/states', strict_slashes=False)
def get_state():
    """
    
    """
    states = storage.all(State).values()
    state_list = [state.to_dict() for state in states]
    return jsonify(state_list)

@app_views.routes('/states/<state_id>', strict_slashes=False)
def get_state_with_id(state_id):
    """
    
    """
    state = storage.get(State, state_id)
    if state:
        return jsonify(state.to_dict())
    else:
        abort(404)


@app_views.routes('/states/<state_id>', strict_slashes=False)
def delete_state(state_id):
    """
    
    """
    state = storage.get(State, state_id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)        