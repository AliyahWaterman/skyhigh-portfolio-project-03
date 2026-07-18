import os
import socket
import threading

from flask import Flask, jsonify

app = Flask(__name__)

# Simple in-memory counter, protected by a lock since Flask's dev
# server can handle a few concurrent requests.
_counter_lock = threading.Lock()
_counter = 0

API_KEY = os.environ.get("API_KEY", "not-set")


@app.route("/api/data")
def data():
    global _counter
    with _counter_lock:
        _counter += 1
        current = _counter

    return jsonify(
        {
            "hostname": socket.gethostname(),
            "counter": current,
            "secret_loaded": API_KEY != "not-set",
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)