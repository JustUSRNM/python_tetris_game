import pygame
import random
from tetris_blocks import Block

#Shapes
shapes = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[2, 1, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]
#Colors of the pieces
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

#variables of the game
width = 700
height = 600
game_width = 100  
game_height = 400  
block_size = 20
 
top_left_x = (width - game_width) // 2
top_left_y = height - game_height - 50

class Tetris:
    level = 2
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    zoom = 20
    x = 100
    y = 60
    current_block = None
    upcoming_block = None

    #properties of the tetris board
    def __init__(self, height, width):
        self.height = height
        self.width = width
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)
    
    #Creating a new block
    def new_block(self):
        self.current_block = Block(3, 0,random.randint(0, len(shapes) - 1))
                           
    def next_block(self):
        self.upcoming_block = Block(3,0,random.randint(0, len(shapes) - 1))
    
    #Checks if the blocks touch the top of the board
    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.current_block.image():
                    if i + self.current_block.y > self.height - 1 or \
                            j + self.current_block.x > self.width - 1 or \
                            j + self.current_block.x < 0 or \
                            self.field[i + self.current_block.y][j + self.current_block.x] > 0:
                        intersection = True
        return intersection
    
    #Checks rows are formed and destroys that line
    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def draw_next_block(self,screen):
    
        font = pygame.font.SysFont("Calibri", 30)
        label = font.render("Next Shape", 1, (128,128,128))

        sx = top_left_x + game_width + 50
        sy = top_left_y+ game_width/2 - 100
        format = self.upcoming_block.image()
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.upcoming_block.image():
                    pygame.draw.rect(screen, shape_colors[self.upcoming_block.color],(sx + j*30, sy + i*30, 30, 30), 0)

    #Drags the current piece to the bottom
    def move_bottom(self):
        while not self.intersects():
            self.current_block.y += 1
        self.current_block.y -= 1
        self.freeze()                
    
    #Moves the block down by a unit
    def moveDown(self):
        self.current_block.y += 1
        if self.intersects():
            self.current_block.y -= 1
            self.freeze()

    #Freezes pieces when they reach the bottom 
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.current_block.image():
                    self.field[i + self.current_block.y][j + self.current_block.x] = self.current_block.color
        self.break_lines() 
        self.block=self.upcoming_block
        self.next_block() 
        if self.intersects(): 
            self.state = "gameover"
    
    #Lets the pieces move horizontaly
    def moveHoriz(self, dx):
        old_x = self.current_block.x
        self.current_block.x += dx
        if self.intersects():
            self.current_block.x = old_x
    
    #Lets the pieces rotate 
    def rotate(self):
        old_rotation = self.current_block.rotation
        self.current_block.rotate()
        if self.intersects():
            self.current_block.rotation = old_rotation