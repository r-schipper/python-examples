from flask import Flask,request,json
# from exchange import Exchange as exchange

import backoff
import configparser
import time

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from datetime import datetime, timedelta

import pandas as pd

import statistics

app = Flask(__name__)
    

@app.route('/test-api', methods = ['GET'])
def test_api():

    return json.dumps('{"test: 123}')


if __name__ == '__main__':
    app.run(host='localhost', port=6000, debug=True)
