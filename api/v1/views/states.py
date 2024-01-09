#!/usr/bin/python3
'''
This module contains the handling of requests related
to the state model
'''
from api.v1.views import app_views
from models import storage
from models.state import State
import json
from flask import make_response, request, abort


@app_views.route('/states',strict_slashes=False)
def states():
    lst = []
    objs = storage.all('State').values()
    for val in objs:
        lst.append(val.to_dict())
    res = make_response(json.dumps(lst))
    res.headers['Content-Type'] = 'application/json'
    return res


@app_views.route('/states', methods=['POST'],strict_slashes=False)
'''
def post_it():
    req = request.get_json(silent=True)
    if req is None:
        res = make_response("Not a JSON")
        res.status = 400
        return res
    if "name" not in req.keys():
        res = make_response("Missing name")
        res.status = 400
        return res
    obj = State(req)
    storage.new(obj)
    storage.save()
    res = make_response(json.dumps(obj.to_dict()))
    res.status = 201
    res.headers['Content-Type'] = 'application/json'
    return res
'''

@app_views.route(
    '/states/<state_id>',
    methods=['GET', 'DELETE', 'PUT'],
    strict_slashes=False
    )
def state_id(state_id):
    if request.method == 'PUT':
        req = request.get_json(silent=True)
        if req is None:
            res = make_response("Not a JSON")
            res.status = 400
            return res
    else:
        val = storage.get(State, state_id)
        if (val is None):
            abort(404)
        if request.method == 'GET':
            res = make_response(val.to_dict())
            res.headers['Content-Type'] = 'application/json'
            return res
        if request.method == 'DELETE':
            val.delete()
            val = dict()
            res = make_response(json.dumps(val))
            res.status = 200
            return res
