from actors import *
import arcade
import constants

class ShipLives(Actor):
    def __init__(self) -> None:
        super().__init__()
        self.cur_pos = 10
        self.mini_ship_width = 0
        self.mini_ship_y = SCREEN_HEIGHT - 40
        self.counter = 0
        self.lives = 0
        

    # Set up the little icons that represent the player lives.
    def draw(self):
        img = "images/ship.png"
        texture = arcade.load_texture(img)

        width = 75 // 3
        height = 99 // 3
        alpha = 130 

        x = self.cur_pos + self.mini_ship_width
        y = self.mini_ship_y
        angle = self.rotation

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)