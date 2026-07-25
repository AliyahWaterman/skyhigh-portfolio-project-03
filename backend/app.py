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