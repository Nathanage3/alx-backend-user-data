#!/usr/bin/env python3
"""A simple flask app
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() ->str:
  """Get /
  Return:
    - The home page's payload.
  """
  return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")