from settings import *

class Block (pg.sprite.Sprite):
    def __init__(self, tetrimino, pos):
        self.tetromino = tetrimino

        super().__init__(tetrimino.tetris.sprite_group)
        self.image = pg.Surface([tile_size,tile_size])
        self.image.fill('orange')

        self.rect = self.image.get_rect()
        self.rect.topleft = pos[0] * tile_size, pos[1] * tile_size
