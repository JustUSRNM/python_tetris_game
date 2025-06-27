from settings import *

class Block (pg.sprite.Sprite):
    def __init__(self, tetrimino, pos):
        self.tetromino = tetrimino
        self.pos = vec(pos) + init_pos_offset

        super().__init__(tetrimino.tetris.sprite_group)
        self.image = pg.Surface([tile_size,tile_size])
        self.image.fill('orange')

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos * tile_size
