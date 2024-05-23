from flask import Flask, request, jsonify
from database import getDBConnection

app = Flask(__name__)

@app.route("/")
def test():
    return ""

if __name__ == '__main__':
    app.run(debug = True)