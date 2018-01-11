from GameFrame import TextObject
import pygame


class F1Text(TextObject):
    def __init__(self, room, x, y, text):
        TextObject.__init__(self, room, x, y, text)
        self.handle_key_events = True

    def key_pressed(self, key):
        if key[pygame.K_F1]:
            self.room.running = False
