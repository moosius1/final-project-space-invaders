from actors import *
import arcade
from constants import *
import math

class ShipBullet(Actor):
    def __init__(self):
        super().__init__()
        self.life = BULLET_LIFE
        self.speed = BULLET_SPEED
        self.radius = BULLET_RADIUS
        self.angle = 0
        self.alive = True
        self.laser_sound = arcade.load_sound("sounds/laser.wav")

    def draw(self):
        img = "images/laser.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 255 # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

    def advance(self):
        super().advance()
        self.life -= 1

    def fire(self):
        self.velocity.dx = math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle)) * self.speed