#!/usr/bin/python3
'''api status'''

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status():
    '''return stuff'''
    return jsonify({"status": "OK"})
