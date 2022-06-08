import json
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)


@app.get("/stockdata/TSLA")
def get_TSLA():
    with open('src/database/TSLA.json') as f:
        data = json.load(f)
    response = jsonify(data)
    return response

@app.get("/stockdata/AMZN")
def get_AMZN():
    with open('src/database/AMZN.json') as f:
        data = json.load(f)
    response = jsonify(data)
    return response

@app.get("/stockdata/AAPL")
def get_AAPL():
    with open('src/database/AAPL.json') as f:
        data = json.load(f)
    response = jsonify(data)
    return response

@app.get("/stockdata/AMD")
def get_AMD():
    with open('src/database/AMD.json') as f:
        data = json.load(f)
    response = jsonify(data)
    return response

@app.get("/stockdata/NVDA")
def get_NVDA():
    with open('src/database/NVDA.json') as f:
        data = json.load(f)
    response = jsonify(data)
    return response

@app.get("/stockdata/MSFT")
def get_MSFT():
    with open('src/database/MSFT.json') as f:
        data = json.load(f)
    response = jsonify(data)
    return response

@app.get("/stockdata/FB")
def get_FB():
    with open('src/database/FB.json') as f:
        data = json.load(f)
    response = jsonify(data)
    return response

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)