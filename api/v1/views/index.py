#!/usr/bin/python3
'''
This is the base view in the application. It includes
routes that require working with all the models in the
storage
'''
from api.v1.views import app_views
from flask import make_response
import json
from models import storage


@app_views.route('/status')
def status():
    state = json.dumps({"status": "OK"})
    resp = make_response(state)
    resp.headers['Content-Type'] = 'application/json'
    return resp


@app_views.route('/stats')
def stats():
    stat = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    val = json.dumps(stat)
    resp = make_response(val)
    resp.headers['Content-Type'] = 'application/json'
    return resp
