import pygame as pg

vec = pg.math.Vector2

fps = 60
field_color = (48, 39, 32)

tile_size = 50
field_size = field_w, field_h = 10, 20
field_res = field_w * tile_size, field_h * tile_size

init_pos_offset = vec(field_size) // 2

tetrominoes = {
    't': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'o': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'j': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'l': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'i': [(0, 0), (0, 1), (0, -1), (0, -2)],
    's': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}