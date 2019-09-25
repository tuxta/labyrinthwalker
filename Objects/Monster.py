import pygame
from GameFrame import RoomObject


class Monster(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image('monster.png')
        self.set_image(image, 32, 32)

        # - Set Monster moving left 6 pixels per frame - #
        self.x_speed = -6
        # - Listen for collisions with Block objects - #
        self.register_collision_object('Block')

    def handle_collision(self, other, other_type):
        # - Reverse Direction when encountering a Block - #
        self.x_speed *= -1
