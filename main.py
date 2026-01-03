import requests
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
db = SQLAlchemy(app)



class user_id(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    spotify_linked = db.Column(db.Boolean,default = False)
    YTmusic_linked = db.Column(db.Boolean, default =False)
    
    def __repr__(self):
        return '<User %r>' % self.id


@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True) 
    app.run(port=5500)

@app.route("/callback", methods=["POST", "GET"])
def callback():
    if request.method == "POST":
        data = request.json or request.form
        print("Callback received:", data)
        return {"status": "success"}, 200
    else:
        return "<p>GET callback received</p>"

