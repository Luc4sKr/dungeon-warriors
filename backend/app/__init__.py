import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app)
app.config.from_object("config")

db = SQLAlchemy(app)
jwt = JWTManager(app)
ma = Marshmallow(app)

migrate = Migrate(app, db)

APP_PATH = os.path.dirname(f"{os.path.abspath(__file__)}")

from .models.weapon import Weapon
from .models.player import Player
from .models.character import Character 

from .models import *
from .views import *
from .routes import *