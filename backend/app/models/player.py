import datetime

from app import db, ma
from marshmallow import fields

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    profile_image = db.Column(db.Text, nullable=True)
    
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())
    max_score = db.Column(db.Integer, nullable=False, default=0)
    coins = db.Column(db.Integer, nullable=False, default=0)


class PlayerSchema(ma.Schema):
    class Meta:
        model = Player
    id = fields.Integer()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
    image = fields.Str()
    
    created_on = fields.DateTime()
    max_score = fields.Integer()
    coins = fields.Integer()


player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)