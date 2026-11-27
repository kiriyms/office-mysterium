import json
from flask import Response

def get_items():
    print("getting items...")
    items = [{ "name": "scissors", "damage": 10 }, { "name": "pencil", "damage": 5 }]
    json_response = json.dumps(items)
    http_response = Response(response=json_response, status=200, mimetype="application/json")
    return http_response