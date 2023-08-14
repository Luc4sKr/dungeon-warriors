from app import db, ma, fields


class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    #image_path = db.Column(db.String(120), unique=True, nullable=False)
    damage = db.Column(db.Integer, nullable=False)


class WeaponSchema(ma.Schema):
    class Meta:
        model = Weapon
    id = fields.Integer()
    name = fields.Str()
    #image_path = fields.Str()
    damage = fields.Integer()

weapon_schema = WeaponSchema()
weapons_schemas = WeaponSchema(many=True)