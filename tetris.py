from settings import *
import math
from tetrimino import Tetrimino

class Tetris:
    def __init__(self,app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetrimino = Tetrimino(self)
        self.speed_up = False

    def check_full_lines(self):
        row = field_h - 1
        for y in range(field_h - 1, -1, -1):
            for x in range(field_w):
                self.field_array[row][x] = self.field_array[y][x]
                
                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x, y)

            if sum(map(bool, self.field_array[y])) < field_w:
                row -= 1
            else:
                for x in range(field_w):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0

    def put_tetromino_blocks_in_array(self):
        for block in self.tetrimino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(field_w)] for y in range(field_h)]

    def check_tetrimono_landing(self):
        if self.tetrimino.landing:
            self.speed_up = False
            self.put_tetromino_blocks_in_array()
            self.tetrimino = Tetrimino(self)

    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetrimino.move(direction='left')
        elif pressed_key == pg.K_RIGHT:
            self.tetrimino.move(direction='right')
        elif pressed_key == pg.K_UP:
            self.tetrimino.rotate()
        elif pressed_key == pg.K_DOWN:
            self.speed_up = True

    def draw_grid(self):
        for x in range(field_w):
            for y in range(field_h):
                pg.draw.rect(self.app.screen, 'black',
                             (x * tile_size, y * tile_size, tile_size, tile_size), 1)

    def update(self):
        trigger = [self.app.anim_trigger, self.app.fast_anim_trigger][self.speed_up]
        if trigger:
            self.check_full_lines()
            self.tetrimino.update()
            self.check_tetrimono_landing()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()    
        self.sprite_group.draw(self.app.screen)