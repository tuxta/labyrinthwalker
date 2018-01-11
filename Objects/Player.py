import pygame
from GameFrame import RoomObject


class Player(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.playerUp = self.load_image('player_up.png')
        self.playerDown = self.load_image('player_down.png')
        self.playerLeft = self.load_image('player_left.png')
        self.playerRight = self.load_image('player_right.png')
        self.set_image(self.playerDown, 18, 32)

        self.depth = 5

        self.handle_key_events = True

        # -- Register the objects with which -- #
        # -- this object handles collisions  -- #
        self.register_collision_object('Block')
        self.register_collision_object('Goal')
        self.register_collision_object('Monster')

    def handle_collision(self, other):
        other_type = type(other).__name__
        if other_type == 'Block':
            self.blocked()
        elif other_type == 'Goal':
            self.room.running = False
        elif other_type == 'Monster':
            self.room.update_score(-1)
            self.x = self.room.home_x
            self.y = self.room.home_y

    def key_pressed(self, key):

        if key[pygame.K_LEFT]:
            self.set_image(self.playerLeft, 18, 32)
            self.x -= 4
        elif key[pygame.K_RIGHT]:
            self.set_image(self.playerRight, 18, 32)
            self.x += 4
        elif key[pygame.K_UP]:
            self.set_image(self.playerUp, 18, 32)
            self.y -= 4
        elif key[pygame.K_DOWN]:
            self.set_image(self.playerDown, 18, 32)
            self.y += 4
