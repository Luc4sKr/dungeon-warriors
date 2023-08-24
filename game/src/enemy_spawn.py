from .enemy import Enemy

class EnemySpawn:
    def __init__(self, obj_handler):
        self.obj_handler = obj_handler
        self.spawn_points = []
        

    def add(self, point):
        self.spawn_points.append(point)

    def check_enemies(self):
        if len(self.obj_handler.enemy_group.sprites()) <= 0:
            self.spawn()

    def spawn(self):
        for point in self.spawn_points:
            enemy = Enemy(self.obj_handler, self.obj_handler.enemy_anim, "assets/sprites/enemies/demon/idle/sprite-1.png", point, 5, 50)
            self.obj_handler.enemy_group.add(enemy)
        