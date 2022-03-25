import arcade

class KeyboardService:
    def check_keys(self):
            """
            This function checks for keys that are being held down.
            You will need to put your own method calls in here.
            Increment/Decrement rotation and speed of the ship
            """
            self.held_keys = set()
            print(self.held_keys)
            if arcade.key.LEFT in self.held_keys:
                self.ship.move_left()
                print("left")

            if arcade.key.RIGHT in self.held_keys:
                self.ship.move_right()
                print("right")