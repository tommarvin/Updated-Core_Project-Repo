from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)

api = 'http://4-service:5503'

DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='TM', password='root', server='35.189.93.20', database='core_project')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABSE_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'TEM_SK123'


from application import routes