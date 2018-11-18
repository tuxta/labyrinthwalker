from GameFrame import Level
from Objects.F1Text import F1Text
from Objects.ExitText import ExitText


class WelcomeScreen(Level):

    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # - Set Background image - #
        self.set_background_image('welcome_background.jpg')

        # - Add Text - #
        self.f1_text = F1Text(self, 20, 200, 'Press F1 to continue')
        self.f1_text.depth = 1000
        self.f1_text.colour = (0, 0, 0)
        self.f1_text.update_text()
        self.add_room_object(self.f1_text)

        self.exit_text = ExitText(self, 20, 300, 'Press Esc to exit the game')
        self.exit_text.depth = 1000
        self.exit_text.colour = (0, 0, 0)
        self.exit_text.update_text()
        self.add_room_object(self.exit_text)
