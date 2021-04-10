from flask import Flask, Response, request
import random, requests
from application import app






@app.route('/Opponent', methods = ['GET'])
def S3():
    opponent = random.randint(1,5)
    opponent_id=str(opponent)
    return Response(opponent_id, mimetype="text/plain")