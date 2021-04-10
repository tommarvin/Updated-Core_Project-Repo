from flask import Flask, Response, request
import random, requests
from application import app

@app.route('/Weapon', methods = ['GET'])
def Post_Weapon():
    weapon = random.randint(1,5)
    weapon_id=str(weapon)
    return Response(weapon_id, mimetype="text/plain")
