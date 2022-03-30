import arcade
import constants

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
            game_view = GameView()
            self.window.show_view(game_view)
        
        elif key == arcade.key.ENTER:
            game_view = GameView()
            self.window.show_view(game_view)