from api.v1.views import app_views
from models import storage
import json
from flask import make_response


@app_views.route('/states')
def states():
    lst = []
    objs = storage.all('State').values()
    for val in objs:
        lst.append(val.to_dict())
    res = make_response(json.dumps(lst))
    res.headers['Content-Type'] = 'application/json'
    return res


@app_views.route('/states/<state_id>')
def state_id(state_id):
    val = storage.get("State", state_id)
    res = make_response(json.dumps(val.values()))
    res.headers['Content-Type'] = 'application/json'
    return res
