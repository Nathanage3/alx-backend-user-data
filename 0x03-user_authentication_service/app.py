#!/usr/bin/env python3

import jsonify
from flask import Flask


app = Flask(__name__)


@app.route("/", Methods="GET", strict_slashes=False)
def hello():
  message = "Bienvenue"
  return jsonify(message), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")