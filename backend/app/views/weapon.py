from app import db, create_access_token
from flask import request, jsonify
from ..models.weapon import Weapon, weapon_schema, weapons_schemas


def get_weapons():
    weapons = Weapon.query.all()

    if weapons:
        result = weapons_schemas.dump(weapons)
        return jsonify({"message": "successfully fetched", "data": result})
    return jsonify({"message": "nothing found", "data": {}})

def get_weapon(id):
    weapon = Weapon.query.get(id)

    if weapon:
        result = weapon_schema.dump(weapon)
        return jsonify({"message": "sucessfully fetched", "data": result}), 201

    return jsonify({"message": "user don't exist", "data": {}}), 404

def post_weapon():
    data = request.get_json()
    print(data)

    try:
        weapon = Weapon(**data)
        db.session.add(weapon)
        db.session.commit()
        result = weapon_schema.dump(weapon)

        return jsonify({"message": "successfully registered", "data": result}), 201

    except:
        return jsonify({"message": "unable to create", "data": {}}), 500