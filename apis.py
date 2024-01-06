from flask_cors import CORS
from flask import Flask, jsonify,request,json
# from exchange import Exchange as exchange

import backoff
import configparser
import time

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

# Start frontend: 
# - cd frontend
# - npm run dev
    

@app.route('/test-api', methods = ['GET'])
def test_api():
    name = request.args.get('name', None)

    response = {
        "name": name
    }
    return jsonify({"data": response, "status": 200, "message": "successfully"})

    # return jsonify(response), 200

@app.route('/days-ago', methods = ['GET'])
def days_ago_api():
    past_date_str = request.args.get('date_in_the_past', None)

    current_date = datetime.now()

    # Define a past date (replace this with your desired past date)
    past_date = datetime.strptime(past_date_str, "%Y-%m-%d")

    # Calculate the difference in days
    days_ago = (current_date - past_date).days

    response = {
        "daysAgo": days_ago
    }
    return jsonify({"data": response, "status": 200, "message": "successfully"})



if __name__ == '__main__':
    app.run(host='localhost', port=6000, debug=True)
