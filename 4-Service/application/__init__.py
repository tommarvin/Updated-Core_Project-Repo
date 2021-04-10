from flask import Flask 
import requests


app = Flask(__name__)

api = 'http://1-service:5500'
api2 = 'http://2-service:5501'
api3 = 'http://3-service:5502'

from application import routes
