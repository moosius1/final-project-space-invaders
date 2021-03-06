from constants import *
import arcade

class Actor:
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0
        self.alive = True
        self.lives = 0
        self.speed = 0
        self.rotation = 0
        self.rock_explosion = arcade.load_sound("sounds/alien_kill.mp3")
        

    def draw(self):
        """ 
        This class will be override 
        """
        pass

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    #Wrap around object.
    def is_off_screen(self):
        if self.center.x <= -20:
            self.center.x = SCREEN_WIDTH
        elif self.center.x > SCREEN_WIDTH + 20:
            self.center.x = 0
        elif self.center.y <= -20:
            self.center.y = SCREEN_HEIGHT
        elif self.center.y > SCREEN_HEIGHT + 20:
            self.center.y = 0

""" 
This class creates initial position 
"""
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

""" 
This class determines Velocity of elements 
"""
class Velocity:
    def __init__(self):
        self.dx = 0
        self.dy = 0