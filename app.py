from flask import Flask, request, jsonify
from database import getDBConnection

app = Flask(__name__)

@app.route("/")
def test():
    return "testing"