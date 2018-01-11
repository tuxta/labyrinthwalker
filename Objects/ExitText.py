from GameFrame import TextObject
from GameFrame import Globals
import pygame


class ExitText(TextObject):
    def __init__(self, room, x, y, text):
        TextObject.__init__(self, room, x, y, text)
        self.handle_key_events = True

    def key_pressed(self, key):
        if key[pygame.K_ESCAPE]:
            self.room.running = False
            Globals.running = False
            Globals.exiting = True
