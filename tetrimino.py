from settings import *
from blocks import Block

class Tetrimino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = 't'
        self.block = [Block(self, pos) for pos in tetrominoes[self.shape]]

    def update(self):
        pass