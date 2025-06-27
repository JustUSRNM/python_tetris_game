from settings import *
from blocks import Block

class Tetrimino:
    def __init__(self, tetris):
        self.tetris = tetris
        Block(self, (4,7))

    def update(self):
        pass