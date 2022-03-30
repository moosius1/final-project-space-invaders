from actors import *
import arcade
from constants import *
import math

class FirstAliens(Actor):
    def __init__(self):
        super().__init__()
        self.speed = ALIEN_SPEED
        self.radius = ALIEN_RADIUS
        self.center.x = 100
        self.center.y = SCREEN_HEIGHT - 100
        self.alive = True
        self.velocity.dx = ALIEN_SPEED
        self.velocity.dy = ALIEN_SPEED_Y

    def draw(self):
        img = "images/first_alien.png"
        texture = arcade.load_texture(img)

        width = 50
        height = 50
        alpha = 255

        x = self.center.x
        y = self.center.y
        angle = 0

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

    def hit(self):
        return 550


    