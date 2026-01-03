import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():

@app.route("/callback", methods=["POST", "GET"])
def callback():
    if request.method == "POST":
        data = request.json or request.form
        print("Callback received:", data)
        return {"status": "success"}, 200
    else:
        return "<p>GET callback received</p>"

