import constants
import arcade
from game import *
        


def main():
    """Main function"""
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    instructions_view = InstructionView()
    arcade.play_sound(instructions_view.intro)
    window.show_view(instructions_view)
    arcade.run()

if __name__ == "__main__":
    main()