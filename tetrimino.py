from settings import *
from blocks import Block
import random

class Tetrimino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(tetrominoes.keys()))
        self.blocks = [Block(self, pos) for pos in tetrominoes[self.shape]]

    def move(self, direction):
        move_direction = move_directions[direction]
        for block in self.blocks:
            block.pos += move_direction

    def update(self):
        self.move(direction='down')