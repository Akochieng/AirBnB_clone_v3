#!/usr/bin/python3
'''
This module instantiates Flask and serves as the main
entry point of the web application.
'''
from os import environ
from flask import Flask, make_response
from models import storage
from api.v1.views import app_views
import json


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def cease_session(exception=None):
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    msg = json.dumps({
        "error": "Not found"
    })
    res = make_response(msg)
    res.headers['Content-Type'] = 'application/json'
    return res


if __name__ == '__main__':
    hostip = environ.get('HBNB_API_HOST', '0.0.0.0')
    theport = environ.get('HBNB_API_PORT', 5000)
    app.run(host=hostip, port=theport, threaded=True, debug=True)
