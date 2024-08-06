#!/usr/bin/python3
"""objects that handles all default RESTFul API actions"""
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves the list of all State objects"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """ Retrieves a State object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """ Delete a State object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}, 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def add_state():
    """Creates a State"""
    if not request.is_json:
        abort(400, description="Not a JSON")

    state_data = request.get_json()
    if 'name' not in state_data:
        abort(400, description="Missing name")

    new_state = State(**state_data)
    storage.new(new_state)
    storage.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """ Updates a State object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    if not request.is_json:
        abort(400, description="Not a JSON")

    state_data = request.get_json()
    ignore_keys = ["id", "created_at", "updated_at"]
    for key, value in state_data.items():
        if key not in ignore_keys:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
