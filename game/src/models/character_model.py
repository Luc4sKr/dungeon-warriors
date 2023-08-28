from .weapon_model import WeaponModel

class CharacterModel:
    def __init__(self, id, life, strength, speed, weapon) -> None:
        self.id = id
        self.life = life
        self.strength = strength
        self.speed = speed

        self.weapon = WeaponModel(**weapon)