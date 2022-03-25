from actors import *
import arcade
from constants import *

class Ship(Actor):
    def __init__(self):
        super().__init__()
        self.center.x = SCREEN_WIDTH // 2
        self.center.y = 50
        self.radius = SHIP_RADIUS
        self.lives = SHIP_LIVES

    def draw(self):
        img = "images/ship.png"
        texture = arcade.load_texture(img)

        width = 75
        height = 99
        alpha = 255 # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.rotation

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

    def move_left(self):
        self.center.x -= 5

    def move_right(self):
        self.center.x += 5

    def hit(self):
        self.lives -= 1

    def is_off_screen(self):
        return super().is_off_screen()        