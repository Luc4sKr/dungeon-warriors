from flask import request, jsonify
from app import db, create_access_token
from ..models.player import Player, player_schema, players_schema
from werkzeug.security import generate_password_hash, check_password_hash


def get_players():
    players = Player.query.all()

    if players:
        result = players_schema.dump(players)
        return jsonify({"message": "successfully fetched", "data": result})
    return jsonify({"message": "nothing found", "data": {}})

def get_player(id):
    player = Player.query.get(id)

    if player:
        result = player_schema.dump(player)
        return jsonify({"message": "sucessfully fetched", "data": result}), 201

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

    print(data)

    data["password"] = generate_password_hash(data["password"])
    
    username = data["username"]
    email = data["email"]
    password = generate_password_hash(data["password"])
    max_socre = 0
    coins = 0
    weapon_id = data["weapon_id"]

    try:
        player = Player(username=username, email=email, password=password, max_score=max_socre, coins=coins, weapon_id=weapon_id)
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