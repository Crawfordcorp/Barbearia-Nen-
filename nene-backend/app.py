
from flask import Flask, request, jsonify
from flask_cors import CORS
from models.user import create_user, login_user
from models.appointment import create_appointment, list_appointments

app = Flask(__name__)
CORS(app)

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    return jsonify(create_user(data["name"], data["email"], data["password"]))

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    return jsonify(login_user(data["email"], data["password"]))

@app.route("/api/appointments", methods=["POST"])
def book():
    data = request.get_json()
    return jsonify(create_appointment(
        user_id=data["user_id"],
        barber=data["barber"],
        service=data["service"],
        date=data["date"],
        price=data["price"]
    ))

@app.route("/api/appointments", methods=["GET"])
def get_appointments():
    return jsonify(list_appointments())

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
