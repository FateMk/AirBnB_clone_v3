#!/usr/bin/pyhton3
"""
Index model holds the endpoint (route)
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status/')
def status():
    """Example endpoint returns status
    returns the current status of the API
    ---
    definitions:
      status:
        type: object
      Color:
        type: string
      items:
        $ref: '#/definitions/Color'
    responses:
      200:
        description: dictionary with 'status' as key and 'ok' as keyvalue
        schema:
          $ref: '#/definitions/State'
        examples:
            {"status": "OK"}
    """
    return jsonify({"status": "OK"})
