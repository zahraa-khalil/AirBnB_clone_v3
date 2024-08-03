#!/usr/bin/python3
"""a script that starts a Flask web application"""

import os
import sys
# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, Blueprint

app = Flask(__name__)

from api.v1.views import app_views
app.register_blueprint(app_views)

from models import storage




# Define the teardown method
@app.teardown_appcontext
def close_storage():
    storage.close()


if __name__ == "_main_":
# Get the host and port from environment variables, with defaults if not set
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
    