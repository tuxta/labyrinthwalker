from GameFrame import Level, Globals
from Objects.GameOverText import GameOverText


class GameOver(Level):

    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # - Set Background image - #
        self.set_background_image("background.jpg")

        # - Add Text - #
        self.GO_Text = GameOverText(self, Globals.SCREEN_WIDTH/4, Globals.SCREEN_HEIGHT/2 - 100, 'Game Over - Press Space')
        self.GO_Text.depth = 1000
        self.GO_Text.colour = (0, 0, 0)
        self.GO_Text.update_text()
        self.add_room_object(self.GO_Text)
