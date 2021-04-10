from flask import Flask, Response, request, jsonify
import random, requests
from application import app, api, api2, api3


@app.route('/Weapon', methods=['GET'])
def Weapon():
    weapon_response = requests.get(api2 + '/Weapon')
    return Response(weapon_response.text, mimetype="text/plain")

@app.route('/Opponent', methods=['GET'])
def Opponent():
    opponent_response = requests.get(api3 + '/Opponent')  
    return Response(opponent_response.text, mimetype="text/plain")

@app.route('/BattleResult', methods=['GET'])
def BattleResult():
    battle = requests.get(api + '/Result')
    BattleStats=battle.json()
    characterhealth = BattleStats['CharacterHealth']
    characterstrength = BattleStats['CharacterStrength']
    weapondamage = BattleStats['WeaponDamage']
    opponenthealth = BattleStats['OpponentHealth']
    opponentstrength = BattleStats['OpponentStrength']

    totalstrength = characterstrength + weapondamage
    user = opponenthealth / totalstrength
    cpu = characterhealth / opponentstrength

    if int(user) < int(cpu):
        result = 1
    elif int(cpu) < int(user):
        result = 2
    else:
        result = 3
    
    Result = str(result)
    
    return Response(Result, mimetype="text/plain")