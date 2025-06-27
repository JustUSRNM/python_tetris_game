from settings import *

class Block (pg.sprite.Sprite):
    def __init__(self, tetrimino, pos):
        self.tetromino = tetrimino
        self.pos = vec(pos) + init_pos_offset

        super().__init__(tetrimino.tetris.sprite_group)
        self.image = pg.Surface([tile_size,tile_size])
        self.image.fill('orange')
        self.rect = self.image.get_rect()
        
    def rotate(self, pivot_pos):
        translated = self.pos - pivot_pos
        rotated = translated.rotate(90)
        return rotated + pivot_pos      

    def set_rect_pos(self):
        self.rect.topleft = self.pos * tile_size

    def update(self):
        self.set_rect_pos()

    def is_collide(self, pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < field_w and y < field_h and (y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True

    
   