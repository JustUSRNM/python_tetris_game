from settings import *
import math
from tetrimino import Tetrimino

class Tetris:
    def __init__(self,app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetrimino = Tetrimino(self)

    def put_tetromino_blocks_in_array(self):
        for block in self.tetrimino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(field_w)] for y in range(field_h)]

    def check_tetrimono_landing(self):
        if self.tetrimino.landing:
            self.put_tetromino_blocks_in_array()
            self.tetrimino = Tetrimino(self)

    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetrimino.move(direction='left')
        elif pressed_key == pg.K_RIGHT:
            self.tetrimino.move(direction='right')
        elif pressed_key == pg.K_UP:
            self.tetrimino.rotate()

    def draw_grid(self):
        for x in range(field_w):
            for y in range(field_h):
                pg.draw.rect(self.app.screen, 'black',
                             (x * tile_size, y * tile_size, tile_size, tile_size), 1)

    def update(self):
        if self.app.anim_trigger:
            self.tetrimino.update()
            self.check_tetrimono_landing()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()    
        self.sprite_group.draw(self.app.screen)