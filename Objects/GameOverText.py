from GameFrame import TextObject
from GameFrame import Globals
import pygame


class GameOverText(TextObject):
    def __init__(self, room, x, y, text):
        TextObject.__init__(self, room, x, y, text)
        self.handle_key_events = True
        Globals.LIVES = 3

    def key_pressed(self, key):
        if key[pygame.K_SPACE]:
            self.room.running = False

