from app import db, ma
from marshmallow import fields
from .weapon import Weapon, WeaponSchema

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    life = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)

    weapon_id = db.Column(db.Integer, db.ForeignKey(Weapon.id), nullable=False)
    weapon = db.relationship("Weapon", backref="weapon")


class CharacterSchema(ma.Schema):
    class Meta:
        model: Character
    id = fields.Integer()
    life = fields.Integer()
    strength = fields.Integer()
    speed = fields.Integer()
    weapon = fields.Nested(WeaponSchema())


character_schema = CharacterSchema()
characters_schema = CharacterSchema(many=True)