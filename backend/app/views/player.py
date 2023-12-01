import os
import uuid
from flask import request, jsonify, send_file
from app import APP_PATH, db, create_access_token
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

def delete_player(id):
    player_obj = Player.query.filter_by(id=id).first()

    if player_obj == None:
        return jsonify({"message": "not found", "data": {}}), 404
    
    try:
        db.session.delete(player_obj)
        db.session.commit()
        return jsonify({"message": "Player deleted successfully", "data": {}}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error deleting player", "data": {}}), 500
    
def save_profile_image():
    if "profile_image" not in request.files:
        return jsonify({"message": f"No files sent:", "data": {}}), 400
    
    try:
        file = request.files["profile_image"]
        random_name = str(uuid.uuid4())
        file_extension = os.path.splitext(file.filename)[1]
        filename = f"{random_name}{file_extension}"
        image_path = f"img/profile/{filename}"
        file_path = f"{APP_PATH}/{image_path}"

        print(image_path)
        print(file_path)

        file.save(file_path)
        return jsonify({"message": "successfully save image", "data": image_path}), 201
    
    except Exception as e:
        return jsonify({"message": f"erro: {e}", "data": {}})

def get_profile_image(player_id):
    player_obj = Player.query.filter_by(id=player_id).first()

    print(player_obj)

    if player_obj:
        path = f"{APP_PATH}/{player_obj.profile_image}"
        print(path)
        return send_file(path, mimetype='image/gif')

def register():
    data = request.get_json()

    username = data["username"]
    email = data["email"]
    password = generate_password_hash(data["password"])
    profile_image_url = data["profile_image_url"]

    try:
        player = Player(username=username, email=email, password=password, profile_image=profile_image_url)
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


