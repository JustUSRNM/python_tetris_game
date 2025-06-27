from settings import *
import math
from tetrimino import Tetrimino

class Tetris:
    def __init__(self,app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.tetrimino = Tetrimino(self)

    def draw_grid(self):
        for x in range(field_w):
            for y in range(field_h):
                pg.draw.rect(self.app.screen, 'black',
                             (x * tile_size, y * tile_size, tile_size, tile_size), 1)

    def update(self):
        self.tetrimino.update()
        self.sprite_group.update

    def draw(self):
        self.draw_grid()    
        self.sprite_group.draw(self.app.screen)