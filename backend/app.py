import os
import socket
import threading
import sys

from flask import Flask, jsonify

app = Flask(__name__)

_counter_lock = threading.Lock()
_counter = 0

API_KEY = os.environ.get("API_KEY", "not-set")


@app.route("/api/data")
def data():
    global _counter
    with _counter_lock:
        _counter += 1
        count = _counter

    return jsonify(
        {
            "hostname": socket.gethostname(),
            "counter": count,
            "secret_loaded": API_KEY != "not-set",
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/api/info")
def info():
    return jsonify(
        {
            "service": "skyhigh-backend",
            "version": "1.0.0",
            "hostname": socket.gethostname(),
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
