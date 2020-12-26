import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

# Flask initialization
app = Flask(__name__)

# Initialze firebase
cred = credentials.Certificate('serviceacc.json')
default_app = initialize_app(cred)

# Initialize firestore DB
db = firestore.client()

@app.route("/", methods=["GET"])
def home():
    return jsonify({ "meefee": 3343 }), 200

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, port=port)

