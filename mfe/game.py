from actors import *
from ship import *
from typing_extensions import Self
import arcade
from constants import *
from ship_bullet import ShipBullet
from first_aliens import FirstAliens
from second_aliens import SecondAliens
from ship_lives import ShipLives
from third_aliens import ThirdAliens
from ship_lives import ShipLives


# Creating MainGame class
class MainGame(arcade.View):
    def __init__(self):
        super().__init__()
        
        """  
        Loading the background image 
        """
        self.background = arcade.load_texture("images/space.png")
        self.held_keys = set()

        """ 
        Create all attributes for the game
        bullets, Ship, Aliens, etc. 
        """
        self.ship = Ship()
        self.bullets = []
        self.first_aliens = []
        self.second_aliens = []
        self.third_aliens = []
        self.ship_lives = []

        """ 
        Create three rows of aliens 
        """
        self.first_x = 80
        for i in range(ALIENS):
            first_alien = FirstAliens()
            first_alien.draw()
            first_alien.center.x = self.first_x
            self.first_aliens.append(first_alien)

            second_alien = SecondAliens()
            second_alien.draw()
            second_alien.center.x = self.first_x
            self.second_aliens.append(second_alien)

            third_alien = ThirdAliens()
            third_alien.draw()
            third_alien.center.x = self.first_x
            self.first_x += 80
            self.third_aliens.append(third_alien)

        """
        Draw Ship Lives
        """
        mini_ex = 0
        for i in range(SHIP_LIVES):
            extra = ShipLives()
            mini_ex += 35
            extra.cur_pos += mini_ex
            extra.draw()
            self.ship_lives.append(extra)

        
    # Creating on_draw() function to draw on the screen
    def on_draw(self):
        arcade.start_render()
        
        # Drawing the background image
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        """ 
        Draw all elements of the Game
        Ship, Bullets, Aliens, etc. 
        """

        self.ship.draw()

        for bullet in self.bullets:
            bullet.draw()

        for first_alien in self.first_aliens:
            first_alien.draw()

        for second_alien in self.second_aliens:
            second_alien.draw()

        for third_alien in self.third_aliens:
            third_alien.draw()

        for extra in self.ship_lives:
            extra.draw()

    def update(self, delta_time):
        
        self.check_keys()

        self.check_off_screen()

        """ 
        Move bullets 
        """
        for bullet in self.bullets:
            bullet.advance()
            if bullet.life <= 0:
                bullet.alive = False

        self.check_collisions()

        """ 
        Move Three rows of Aliens 
        """
        for first_alien in self.first_aliens:
            first_alien.advance()
            if (first_alien.center.x > (SCREEN_WIDTH - 25)) or (first_alien.center.x < 25):
                first_alien.velocity.dx = (first_alien.velocity.dx * -1)

        for second_alien in self.second_aliens:
            second_alien.advance()
            if (second_alien.center.x > (SCREEN_WIDTH - 25)) or (second_alien.center.x < 25):
                second_alien.velocity.dx = (second_alien.velocity.dx * -1)

        for third_alien in self.third_aliens:
            third_alien.advance()
            if (third_alien.center.x > (SCREEN_WIDTH - 25)) or (third_alien.center.x < 25):
                third_alien.velocity.dx = (third_alien.velocity.dx * -1)

        """ 
        Update Lives (mini ships) 
        """
        for extra in self.ship_lives:
            extra.draw()
            if extra.lives >= SHIP_LIVES:
                extra.alive = False

        
        """ 
        Game Over You Win Screen
        """
        if len(self.first_aliens) <= 0 and len(self.ship_lives) >= 0:
            view = VictoryView()
            self.window.show_view(view)
            arcade.play_sound(view.victory)
        
        """ 
        Game Over You Lose Screen 
        """
        if len(self.ship_lives) == 0:
            view = GameOverView()
            self.window.show_view(view)
            arcade.play_sound(view.game_over)


    def check_keys(self):
            """
            This function checks for keys that are being held down.
            Motion of the Ship
            """
            if arcade.key.LEFT in self.held_keys:
                self.ship.move_left()

            if arcade.key.RIGHT in self.held_keys:
                self.ship.move_right()

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        Shooting bullets
        """
        if self.ship.alive:
            self.held_keys.add(key)

            #Create object for bullet and fire
            bullet = ShipBullet()

            #Shoot!
            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                bullet = ShipBullet()
                bullet.center.x = self.ship.center.x
                bullet.center.y = self.ship.center.y
                bullet.angle = 90
                bullet.fire()
                self.bullets.append(bullet)
                arcade.play_sound(bullet.laser_sound)
            bullet.velocity.dx += self.ship.velocity.dx
            bullet.velocity.dy += self.ship.velocity.dy

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)

    def check_off_screen(self):
        """
        Checks to see if Ship  have left the screen.
        """
        self.ship.is_off_screen()

    def check_collisions(self):
        """
        Checks to see if bullets have hit Aliens.
        Updates scores and removes dead items.
        """       
        for first_alien in self.first_aliens:
            """
            Check collision between bullet and Aliens
            """
            for bullet in self.bullets:
                # Make sure they are both alive before checking for a collision
                if bullet.alive and first_alien.alive:
                    too_close = bullet.radius + first_alien.radius

                    if (abs(bullet.center.x - first_alien.center.x) < too_close and abs(bullet.center.y - first_alien.center.y) < too_close):
                        first_alien.alive = False
                        bullet.alive = False
                        arcade.play_sound(first_alien.rock_explosion)

            """ 
            Make sure both ship and First Aliens are alive before checking for a collision 
            """
            if self.ship.alive and first_alien.alive:
                too_close = self.ship.radius + first_alien.radius

                if (abs(self.ship.center.x - first_alien.center.x) < too_close and abs(self.ship.center.y - first_alien.center.y) < too_close):
                    # its a crash!
                    #self.score += self.ship.hit()
                    first_alien.alive = False
                    if self.ship_lives:    
                        self.ship_lives.pop()
                    else:
                        self.ship.alive = False
                        arcade.play_sound(self.ship.ship_explosion)
                    arcade.play_sound(first_alien.rock_explosion)

        for second_alien in self.second_aliens:
            """
            Check collision between bullet and asteroids
            """
            for bullet in self.bullets:
                # Make sure they are both alive before checking for a collision
                if bullet.alive and second_alien.alive:
                    too_close = bullet.radius + second_alien.radius

                    if (abs(bullet.center.x - second_alien.center.x) < too_close and abs(bullet.center.y - second_alien.center.y) < too_close):
                        second_alien.alive = False
                        bullet.alive = False
                        arcade.play_sound(second_alien.rock_explosion)

            # Make sure both ship and Second Aliens are alive before checking for a collision
            if self.ship.alive and second_alien.alive:
                too_close = self.ship.radius + second_alien.radius

                if (abs(self.ship.center.x - second_alien.center.x) < too_close and abs(self.ship.center.y - second_alien.center.y) < too_close):
                    # its a crash!
                    #self.score += self.ship.hit()
                    second_alien.alive = False
                    if self.ship_lives:    
                        self.ship_lives.pop()
                    else:
                        self.ship.alive = False
                        arcade.play_sound(self.ship.ship_explosion)
                    arcade.play_sound(second_alien.rock_explosion)
        
        for third_alien in self.third_aliens:
            """
            Check collision between bullet and asteroids
            """
            for bullet in self.bullets:
                # Make sure they are both alive before checking for a collision
                if bullet.alive and third_alien.alive:
                    too_close = bullet.radius + third_alien.radius

                    if (abs(bullet.center.x - third_alien.center.x) < too_close and abs(bullet.center.y - third_alien.center.y) < too_close):
                        third_alien.alive = False
                        bullet.alive = False
                        arcade.play_sound(third_alien.rock_explosion)

            # Make sure both ship and Third Aliens are alive before checking for a collision
            if self.ship.alive and third_alien.alive:
                too_close = self.ship.radius + third_alien.radius

                if (abs(self.ship.center.x - third_alien.center.x) < too_close and abs(self.ship.center.y - third_alien.center.y) < too_close):
                    # its a crash!
                    #self.score += self.ship.hit()
                    third_alien.alive = False
                    if self.ship_lives:    
                        self.ship_lives.pop()
                    else:
                        self.ship.alive = False
                        arcade.play_sound(self.ship.ship_explosion)
                    arcade.play_sound(third_alien.rock_explosion)
                        
        #This method removes elements from their arrays         
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or Aliens from the list.
        """ 
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for first_alien in self.first_aliens:
            if not first_alien.alive:
                self.first_aliens.remove(first_alien)

        for second_alien in self.second_aliens:
            if not second_alien.alive:
                self.second_aliens.remove(second_alien)

        for third_alien in self.third_aliens:
            if not third_alien.alive:
                self.third_aliens.remove(third_alien)


"""
Instructions of the Game Screen
"""
class InstructionView(arcade.View):
    def __init__(self):
        super().__init__()
        self.intro = arcade.load_sound("sounds/intro.wav")

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Space Invaders", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.LIGHT_GRAY, font_size=40, anchor_x="center")
        arcade.draw_text("(Team 08 Version)", SCREEN_WIDTH / 2, 290,
                         arcade.color.LIGHT_GRAY, font_size=15, italic="True", anchor_x="center")
        arcade.draw_text("Enter to Start a New Game", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-100,
                         arcade.color.LIGHT_GRAY, font_size=20, anchor_x="center")

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.ENTER and key_modifiers == arcade.key.MOD_SHIFT:
            game_view = MainGame()
            self.window.show_view(game_view)

        
        elif key == arcade.key.ENTER:
            game_view = MainGame()
            self.window.show_view(game_view)


"""
Game Over Class
"""
class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("images/you_lose.png")
        self.game_over = arcade.load_sound("sounds/game_over.wav")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        arcade.draw_text("Enter to Try Again", SCREEN_WIDTH/2, SCREEN_HEIGHT/4-75,
                         arcade.color.LIGHT_GRAY, font_size=20, anchor_x="center")

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.ENTER and key_modifiers == arcade.key.MOD_SHIFT:
            game_view = MainGame()
            self.window.show_view(game_view)
        
        elif key == arcade.key.ENTER:
            game_view = MainGame()
            self.window.show_view(game_view)


class VictoryView(arcade.View):
    """ View to show when game is finished """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("images/you_win.png")
        self.victory = arcade.load_sound("sounds/victory.mp3")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        arcade.draw_text("Enter to Start Again", SCREEN_WIDTH/2, SCREEN_HEIGHT/4-75,
                         arcade.color.LIGHT_GRAY, font_size=20, anchor_x="center")

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.ENTER and key_modifiers == arcade.key.MOD_SHIFT:
            game_view = MainGame()
            self.window.show_view(game_view)
        
        elif key == arcade.key.ENTER:
            game_view = MainGame()
            self.window.show_view(game_view)