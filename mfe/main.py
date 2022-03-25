from actors import *
from ship import *
from typing_extensions import Self
import arcade
from constants import *
from ship_bullet import ShipBullet
from first_aliens import FirstAliens
from second_aliens import SecondAliens
from third_aliens import ThirdAliens


# Creating MainGame class
class MainGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Loading the background image
        self.background = arcade.load_texture("images/space.png")
        self.held_keys = set()

        self.ship = Ship()
        self.bullets = []
        self.first_aliens = []
        self.second_aliens = []
        self.third_aliens = []

        self.first_x = 80
        for i in range(ALIENS):
            first_alien = FirstAliens()
            first_alien.draw()
            first_alien.center.x = self.first_x
            self.first_x += 80
            self.first_aliens.append(first_alien)

        self.second_x = 80
        for i in range(ALIENS):
            second_alien = SecondAliens()
            second_alien.draw()
            second_alien.center.x = self.second_x
            self.second_x += 80
            self.second_aliens.append(second_alien)

        self.third_x = 80
        for i in range(ALIENS):
            third_alien = ThirdAliens()
            third_alien.draw()
            third_alien.center.x = self.third_x
            self.third_x += 80
            self.third_aliens.append(third_alien)

        
    # Creating on_draw() function to draw on the screen
    def on_draw(self):
        arcade.start_render()
        
        # Drawing the background image
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.ship.draw()

        for bullet in self.bullets:
            bullet.draw()

        for first_alien in self.first_aliens:
            first_alien.draw()

        for second_alien in self.second_aliens:
            second_alien.draw()

        for third_alien in self.third_aliens:
            third_alien.draw()

    def update(self, delta_time):
        
        self.check_keys()

        self.check_off_screen()

        for bullet in self.bullets:
            bullet.advance()
            if bullet.life <= 0:
                bullet.alive = False

        self.check_collisions()

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


    def check_keys(self):
            """
            This function checks for keys that are being held down.
            You will need to put your own method calls in here.
            Increment/Decrement rotation and speed of the ship
            """
            if arcade.key.LEFT in self.held_keys:
                self.ship.move_left()

            if arcade.key.RIGHT in self.held_keys:
                self.ship.move_right()

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
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
            bullet.velocity.dx += self.ship.velocity.dx
            bullet.velocity.dy += self.ship.velocity.dy

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        Increment/Decrement speed after release key.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)

    def check_off_screen(self):
        """
        Checks to see if Ship, bullets and/or asteroids have left the screen.
        """
        self.ship.is_off_screen()

    def check_collisions(self):
        """
        Checks to see if bullets have hit asteroids.
        Updates scores and removes dead items.
        :return:
        """       
        for first_alien in self.first_aliens:
            """
            Check collision between bullet and asteroids
            """
            for bullet in self.bullets:
                # Make sure they are both alive before checking for a collision
                if bullet.alive and first_alien.alive:
                    too_close = bullet.radius + first_alien.radius

                    if (abs(bullet.center.x - first_alien.center.x) < too_close and abs(bullet.center.y - first_alien.center.y) < too_close):
                        first_alien.alive = False
                        bullet.alive = False

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
                        
                        
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or asteroids from the list.
        :return:
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
        


def main():
    """Main function"""
    window = MainGame()
    #window.setup()
    arcade.run()


if __name__ == "__main__":
    main()