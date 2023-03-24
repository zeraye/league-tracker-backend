import os
import json
from pathlib import Path
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/tracker", methods=["GET"])
@cross_origin()
def tracker() -> None:
    with open(Path(os.path.dirname(os.path.realpath(__file__))) / "database" / "points.json", "r") as file:
        points_data = json.load(file)

    return app.response_class(
        response=json.dumps(points_data),
        status=200,
        mimetype="application/json"
    )
