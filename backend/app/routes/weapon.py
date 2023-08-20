from app import app
from ..views import weapon


@app.route("/weapons", methods=["GET"])
def get_weapons():
    return weapon.get_weapons()

@app.route("/weapon/<id>", methods=["GET"])
def get_weapon(id):
    return weapon.get_weapon(id)

@app.route("/weapon", methods=["POST"])
def post_weapon():
    return weapon.post_weapon()