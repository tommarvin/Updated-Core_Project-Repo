from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app 

    def setUp(self):
        db.create_all()
        db.session.add(CharacterHealth(character_name='Character 1', health=100, strength=10, gold=0))
        db.session.add(Weapons(weapon_name='Weapon 1', damage=15))        
        db.session.add(Opponents(opponent_name='Opponent 1', health=120, strength=10))        
        db.session.add(Battle(character_battle=1, weapon_id=1, opponent_id=1))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponses(TestBase):

    def test_generate(self):
        a.get('http://4-service:5503/Weapon', text=1)
        b.get('http://4-service:5503/Opponent', text=1)
        response = self.client.get(url_for('Configure(RND,'))
