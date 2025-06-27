from settings import *
import math
from tetromino import Tetromino

class Tetris:
    def __init__(self,app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        self.next_tetromino = Tetromino(self, current=False)
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
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(field_w)] for y in range(field_h)]

    def check_tetrimono_landing(self):
        if self.tetromino.landing:
            self.speed_up = False
            self.put_tetromino_blocks_in_array()
            self.next_tetromino.current = True
            self.tetromino = self.next_tetromino
            self.next_tetromino = Tetromino(self, current=False)

    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetromino.move(direction='left')
        elif pressed_key == pg.K_RIGHT:
            self.tetromino.move(direction='right')
        elif pressed_key == pg.K_UP:
            self.tetromino.rotate()
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
            self.tetromino.update()
            self.check_tetrimono_landing()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()    
        self.sprite_group.draw(self.app.screen)