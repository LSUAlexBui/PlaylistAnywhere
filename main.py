import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Flask!</h1><p>This replaces Live Server.</p>"

@app.route("/callback", methods=["POST", "GET"])
def callback():
    if request.method == "POST":
        data = request.json or request.form
        print("Callback received:", data)
        return {"status": "success"}, 200
    else:
        return "<p>GET callback received</p>"

if __name__ == "__main__":
    app.run(port=5500)  # Same port Live Server uses by default
