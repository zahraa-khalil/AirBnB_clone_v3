#!/usr/bin/python3
"""a script that starts a Flask web application"""

import os
import sys
from flask import Flask, Blueprint
from api.v1.views import app_views
from models import storage

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage():
    storage.close()


if __name__ == "_main_":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
