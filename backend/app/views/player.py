from flask import request, jsonify
from app import db, create_access_token
from ..models.player import Player, player_schema, players_schema
from werkzeug.security import generate_password_hash, check_password_hash


def get_players():
    players = Player.query.all()

    if players:
        result = players_schema.dump(players)
        return jsonify({"message": "successfully fetched", "data": result}), 200
    return jsonify({"message": "nothing found", "data": {}}), 404

def get_player(id):
    player = Player.query.get(id)

    if player:
        result = player_schema.dump(player)
        return jsonify({"message": "sucessfully fetched", "data": result}), 200
    return jsonify({"message": "nothing found", "data": {}}), 404

def post_player():
    data = request.get_json()
    data["password"] = generate_password_hash(data["password"])

    try:
        player = Player(**data)
        db.session.add(player)
        db.session.commit()
        result = player_schema.dump(player)
        return jsonify({"message": "successfully registered", "data": result}), 201
    except:
        return jsonify({"message": "unable to create", "data": {}}), 500
    
def register():
    data = request.get_json()

    username = data["username"]
    email = data["email"]
    password = generate_password_hash(data["password"])

    try:
        player = Player(username=username, email=email, password=password)
        db.session.add(player)
        db.session.commit()
        result = player_schema.dump(player)
        return jsonify({"message": "successfully registered", "data": result}), 201
    
    except Exception as e:
        return jsonify({"message": "unable to create", "error": e, "data": {}}), 500

def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    player = Player.query.filter(Player.username == username).one()

    if check_password_hash(player.password, password):
        access_token = create_access_token(identity=username)
        return jsonify({"message": "login successfully", "data": access_token})

    return jsonify({"message": "incorrect username or password"})

def update_player(id):
    player_obj = Player.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if ("max_score" in body):
            player_obj.max_score = body["max_score"]

        db.session.add(player_obj)
        db.session.commit()
        return jsonify({"message": "player updated", "data": player_schema.dump(player_obj)})
    except Exception as e:
        return jsonify({"message": "error" + e, "data": {}})