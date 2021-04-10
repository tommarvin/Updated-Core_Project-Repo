from application import app, db
from application.models import *

db.drop_all()
db.create_all()

character1 = Characters(character_name='Character 1', health=100, strength=10, gold=0)
db.session.add(character1)
character2 = Characters(character_name='Character 2', health=80, strength=15, gold=0)
db.session.add(character2)
character3 = Characters(character_name='Character 3', health=60, strength=20, gold=0)
db.session.add(character3)

weapon1 = Weapons(weapon_name='Weapon 1', damage=5)
db.session.add(weapon1)
weapon2 = Weapons(weapon_name='Weapon 2', damage=20)
db.session.add(weapon2)
weapon3 = Weapons(weapon_name='Weapon 3', damage=12)
db.session.add(weapon3)
weapon4 = Weapons(weapon_name='Weapon 4', damage=2)
db.session.add(weapon4)
weapon5 = Weapons(weapon_name='Weapon 5', damage=30)
db.session.add(weapon5)

opponent1 = Opponents(opponent_name='Opponent 1', health=150, strength=10)
db.session.add(opponent1)
opponent2 = Opponents(opponent_name='Opponent 2', health=120, strength=15)
db.session.add(opponent2)
opponent3 = Opponents(opponent_name='Opponent 3', health=100, strength=20)
db.session.add(opponent3)
opponent4 = Opponents(opponent_name='Opponent 4', health=25, strength=30)
db.session.add(opponent4)
opponent5 = Opponents(opponent_name='Opponent 5', health=200, strength=10)
db.session.add(opponent5)

db.session.commit()

