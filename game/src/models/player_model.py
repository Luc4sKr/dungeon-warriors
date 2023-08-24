from .weapon_model import WeaponModel

class PlayerModel:
    def __init__(self, id, username, email, password, created_on, max_score, coins, life, strength, speed, weapon):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.created_on = created_on

        self.max_score = max_score
        self.coins = coins
        self.life = life
        self.strength = strength
        self.speed = speed

        self.weapon = WeaponModel(**weapon)