from settings import *
from tetris import Tetris
import math
import pygame.freetype as ft

class Text:
    def __init__(self, app):
        self.app = app
        self.font = ft.Font(font_dir_path)

    def get_color(self):
        time = pg.time.get_ticks() * 0.001
        n_sin = lambda t: (math.sin(t) * 0.5 + 0.5) * 255
        return n_sin(time * 0.5), n_sin(time * 0.2), n_sin(time * 0.9)

    def draw(self):
        self.font.render_to(self.app.screen, (win_w * 0.595, win_h * 0.02),
                            text='TETRIS', fgcolor=self.get_color(),
                            size=tile_size * 1.65, bgcolor='black')
        self.font.render_to(self.app.screen, (win_w * 0.65, win_h * 0.22),
                            text='next', fgcolor='orange',
                            size=tile_size * 1.4, bgcolor='black')
        self.font.render_to(self.app.screen, (win_w * 0.64, win_h * 0.67),
                            text='score', fgcolor='orange',
                            size=tile_size * 1.4, bgcolor='black')
        self.font.render_to(self.app.screen, (win_w * 0.64, win_h * 0.8),
                            text=f'{self.app.tetris.score}', fgcolor='white',
                            size=tile_size * 1.8)