from settings import *

class Block (pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = vec(pos) + init_pos_offset
        self.next_pos = vec(pos) + next_pos_offset
        self.alive = True

        super().__init__(tetromino.tetris.sprite_group)
        self.image = tetromino.image
        #self.image = pg.Surface([tile_size,tile_size])
        #pg.draw.rect(self.image, 'orange', (1, 1, tile_size - 2, tile_size -2), border_radius = 8)
        self.rect = self.image.get_rect()
        
    def is_alive(self):
        if not self.alive:
            self.kill()    

    def rotate(self, pivot_pos):
        translated = self.pos - pivot_pos
        rotated = translated.rotate(90)
        return rotated + pivot_pos      

    def set_rect_pos(self):
        pos = [self.next_pos, self.pos][self.tetromino.current]
        self.rect.topleft = pos * tile_size

    def update(self):
        self.is_alive()
        self.set_rect_pos()

    def is_collide(self, pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < field_w and y < field_h and (y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True

    
   