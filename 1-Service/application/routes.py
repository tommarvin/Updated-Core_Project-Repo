from application import app, db, api
from application.models import Characters, Weapons, Opponents, Battle
from flask import Flask, request, render_template, Response, redirect, jsonify
import random, requests



@app.route('/', methods = ['GET', 'POST'])
def index():
    num_rounds=[]
    for battles in Battle.query.all():
        num_rounds.append(battles)
    Rnd = len(num_rounds)
    return render_template('index.html', Rnd=Rnd)

@app.route('/Step-1/<Rnd>', methods = ['GET', 'POST'])

def S1(Rnd):
    Rnd = int(Rnd)+1
    return render_template('s1.html', Characters=Characters, Rnd=Rnd)

@app.route('/Configure/<Rnd>/<ID>', methods = ['GET', 'POST'])
def Configure(Rnd,ID):
    Rnd = int(Rnd)
    character = ID 
    weapon_response = requests.get(api + '/Weapon')
    weapon = weapon_response.text
    opponent_response = requests.get(api + '/Opponent')
    opponent = opponent_response.text
    battle = Battle(character_id=character, weapon_id=weapon, opponent_id=opponent)
    db.session.add(battle)
    db.session.commit()
    return redirect(f'/Step-2/{Rnd}')


@app.route('/Step-2/<Rnd>', methods = ['GET', 'POST'])
def S2(Rnd):
    Rnd=int(Rnd)
    for battles in Battle.query.filter_by(id=Rnd):
        weapon = battles.weapon_id

    return render_template('s2.html', Weapons=Weapons, weapon=weapon, Rnd=Rnd)

@app.route('/Step-3/<Rnd>', methods = ['GET', 'POST'])
def S3(Rnd):
    Rnd=int(Rnd)
    for battles in Battle.query.filter_by(id=Rnd):
        opponent = battles.opponent_id
    return render_template('s3.html',Opponents=Opponents, opponent=opponent, Rnd=Rnd)

@app.route('/Result', methods=['GET'])
def result():
    rounds = []
    for battles in Battle.query.all():
        rounds.append(battles)
    Rnd = len(rounds)
    
    battle = Battle.query.filter_by(id=Rnd).first()
    character = Characters.query.filter_by(id=battle.character_id).first()
    weapon = Weapons.query.filter_by(id=battle.weapon_id).first()
    opponent = Opponents.query.filter_by(id=battle.opponent_id).first()
    battlestats = {'CharacterHealth': character.health, 
                   'CharacterStrength': character.strength, 
                   'WeaponDamage': weapon.damage,
                   'OpponentHealth': opponent.health, 
                   'OpponentStrength': opponent.strength}

    return jsonify(battlestats)

@app.route('/Step-4/<Rnd>', methods = ['GET', 'POST'])
def S4(Rnd):
    Rnd=int(Rnd)
    BTL = Battle.query.filter_by(id=Rnd).first()
    char = BTL.character_id
    weap = BTL.weapon_id
    opp = BTL.opponent_id

    result = requests.get(api + '/BattleResult')
    if result.text == '1':
        text1='Congratulations, you won the battle. Your prize is 500 gold coins!'
    elif result.text == '2':
        text1='Unfortunately, you were defeated in battle. You will not recieve a prize...'
    else:
        text1='You and your Opponent were too evenly matched to determine a clear winner, you each are given a prize of 250 gold, congratulations!'

    return render_template('s4.html', text1=text1, char=char, Characters=Characters, weap=weap, Weapons=Weapons, opp=opp, Opponents=Opponents, Rnd=Rnd)


