from app import app
from ..views import player


@app.route("/players", methods=["GET"])
def get_players():
    return player.get_players()

@app.route("/player/<int:id>", methods=["GET"])
def get_player(id):
    return player.get_player(id)

@app.route("/player", methods=["POST"])
def post_player():
    return player.post_player()

@app.route("/player/<int:id>", methods=["PUT"])
def update_player(id):
    return player.update_player(id)

@app.route("/player/<id>", methods=["DELETE"])
def delete_player(id):
    return player.delete_player(id)

@app.route("/player/save_profile_image", methods=["POST"])
def save_profile_image():
    return player.save_profile_image()

@app.route("/player/get_profile_image/<int:player_id>", methods=["GET"])
def get_profile_image(player_id):
    return player.get_profile_image(player_id)

@app.route("/player/register", methods=["POST"])
def register_player():
    return player.register()

@app.route("/player/login", methods=["POST"])
def login_player():
    return player.login()
