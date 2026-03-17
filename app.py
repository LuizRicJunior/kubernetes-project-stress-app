from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/stress")
def stress():
    x = 0
    for i in range(10**7):
        x += i
    return jsonify({"result": x})


@app.route("/slow")
def slow():
    time.sleep(2)
    return {"status": "done", "delay": "2s"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)