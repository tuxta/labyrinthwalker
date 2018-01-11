from GameFrame import Level, TextObject, Globals
from Objects import Goal, Block, BlockDoor, Player, Banner, Monster


class L_Medium(Level):

    def __init__(self, screen):
        Level.__init__(self, screen)

        # - Set Background image - #
        self.set_background_image("background.jpg")

        # - Home location for the player - #
        self.home_x = 18*32
        self.home_y = 15*32

        # - Set up maze, objects 32x32 25x17 - #
        room_objects = [
            'bbbbbbbbbbbbbbbbbbbbbbbbb',
            'b______________________gb',
            'b___bbbbb_d_bbbbbbbb__bdb',
            'b___b___bb_bbb_____b___bb',
            'b___b____b__b___b___b___b',
            'b___bb___b__b___bbb__b__b',
            'b____b___b__b______b___mb',
            'b____b___b__bbbb__b_____b',
            'b____bbbbb_____b__b_____b',
            'b_____m_______b__bbbbbbdb',
            'b____bbbb____b__b_______b',
            'bbbbb_______b_b__b__bb__b',
            'b_____bbbbb_b_b__b__bb__b',
            'b_________b_b_b_____bb__b',
            'b__bbbbbbbbbbbbb__bbbb__b',
            'b________________bp_____b',
            'bbbbbbbbbbbbbbbbbbbbbbbbb'
        ]

        for i, row in enumerate(room_objects):
            for j, obj in enumerate(row):
                if obj == 'b':
                    self.add_room_object(Block(self, j*32, i*32))
                elif obj == 'd':
                    self.add_room_object(BlockDoor(self, j * 32, i * 32))
                elif obj == 'p':
                    self.add_room_object(Player(self, j*32, i*32))
                elif obj == 'g':
                    self.add_room_object(Goal(self, j*32, i*32))
                elif obj == 'm':
                    self.add_room_object(Monster(self, j*32, i*32))

        # - Add Banner for game info (lives) 800x56 - #
        self.add_room_object(Banner(self, 0, 544))

        # - Add Text - #
        self.score_text = TextObject(self, 20, 560, 'Lives: %i' % Globals.LIVES)
        self.score_text.depth = 1000
        self.score_text.colour = (255, 255, 255)
        self.score_text.update_text()
        self.add_room_object(self.score_text)

    def update_score(self, value):
        Globals.LIVES += value
        if Globals.LIVES == 0:
            self.running = False
            self.quitting = True
        self.score_text.text = 'Lives: %i' % Globals.LIVES
        self.score_text.update_text()
