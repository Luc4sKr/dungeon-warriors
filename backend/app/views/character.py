from app import db, create_access_token
from flask import request, jsonify
from ..models.character import Character, character_schema, characters_schema

def get_characters():
    characters = Character.query.all()

    if characters:
        result = characters_schema.dump(characters)
        return jsonify({"message": "successfully fetched", "data": result})
    return jsonify({"message": "nothing found", "data": {}}), 404

def get_character(id):
    character = Character.query.get(id)

    if character:
        result = character_schema.dump(character)
        return jsonify({"message": "sucessfully fetched", "data": result}), 201
    return jsonify({"message": "nothing found", "data": {}}), 404

def post_character():
    data = request.get_json()

    try:
        character = Character(**data)
        db.session.add(character)
        db.session.commit()
        result = character_schema.dump(character)
        return jsonify({"message": "successfully registered", "data": result}), 201
    except:
        return jsonify({"message": "unable to create", "data": {}}), 500