from app import app
from ..views import character


@app.route("/characters", methods=["GET"])
def get_characters():
    return character.get_characters()

@app.route("/character/<id>", methods=["GET"])
def get_character(id):
    return character.get_character(id)

@app.route("/character", methods=["POST"])
def post_character():
    return character.post_character()
