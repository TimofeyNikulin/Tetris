import pygame
import random
from config import BLOCKS, SIZE_OF_BLOCK, COLORS, level, reversed_level


class Field:
    def __init__(self, screen):
        self.screen = screen
        self.slices = []

    def draw_field(self):
        for index_x, box in enumerate(level):
            for index_y, sym in enumerate(box):
                if sym != '*':
                    pygame.draw.rect(self.screen, COLORS[sym], pygame.Rect(
                        index_y * SIZE_OF_BLOCK, index_x * SIZE_OF_BLOCK, SIZE_OF_BLOCK, SIZE_OF_BLOCK))

    def create_block(self):
        type_of_block = random.choice(BLOCKS)
        color = random.choice(list(COLORS.keys()))
        self.coord = []
        if type_of_block == 'I':
            i = random.randint(0, 16)
            slice_b = list('********************')
            slice_b[i: i + 3] = list(color * 4)
            ''.join(slice_b)
            level[0] = slice_b
            self.slices.append(slice_b)
        elif type_of_block == 'O':
            i = random.randint(0, 18)
            slice_a = list('********************')
            slice_b = list('********************')
            slice_a[i: i + 1] = list(color * 2)
            ''.join(slice_a)
            level[0] = slice_b
            slice_b[i: i + 1] = list(color * 2)
            ''.join(slice_b)
            level[1] = slice_b
            self.slices.append(slice_b)

    def move_block(self):
        global reversed_level
        index_rev = reversed_level.index('********************')
        index = 24 - index_rev
        level.pop(index)
        level.insert(0, '********************')
        reversed_level = level[::-1]
