from application import db
from flask_sqlalchemy import SQLAlchemy
from os import getenv



class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(20))
    health = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    gold = db.Column(db.Integer, nullable=False)
    battle = db.relationship('Battle', backref='characters')

class Weapons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weapon_name = db.Column(db.String(20), nullable=False)
    damage = db.Column(db.Integer, nullable=False)
    battle = db.relationship('Battle', backref='weapons')

class Opponents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    opponent_name = db.Column(db.String(20), nullable=False)
    health = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    battle = db.relationship('Battle', backref='opponents')

class Battle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    weapon_id = db.Column(db.Integer, db.ForeignKey('weapons.id'))
    opponent_id = db.Column(db.Integer, db.ForeignKey('opponents.id'))
