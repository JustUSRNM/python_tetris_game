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
    def move_down(self):
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
    def move_horizontal(self, dx):
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

pygame.font.init()

def startGame():
    done = False
    clock = pygame.time.Clock()
    fps = 25
    game = Tetris(20, 10)
    counter = 0

    pressing_down = False
    
    while not done:
        #Create a new block if there is no moving block
        if game.current_block is None:
            game.new_block()
        if game.upcoming_block is None:
            game.next_block()
        counter += 1 #Keeping track if the time 
        if counter > 100000:
            counter = 0
        
        #Moving the block continuously with time or when down key is pressed
        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "start":
                game.move_down()
        
        #Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                if event.key == pygame.K_LEFT:
                    game.move_horizontal(-1)
                if event.key == pygame.K_RIGHT:
                    game.move_horizontal(1)
                if event.key == pygame.K_SPACE:
                    game.move_bottom()
                if event.key == pygame.K_ESCAPE:
                    game.__init__(20, 10)
    
        screen.fill('#FFFFFF')

    #Refreing the game board
        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen, '#B2BEB5', [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(screen, shape_colors[game.field[i][j]],
                                     [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])
                    
        if game.current_block is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.current_block.image():
                        pygame.draw.rect(screen, shape_colors[game.block.color],
                                         [game.x + game.zoom * (j + game.current_block.x) + 1,
                                          game.y + game.zoom * (i + game.cuurent_block.y) + 1,
                                          game.zoom - 2, game.zoom - 2])    
        
        #Showing the score
        font = pygame.font.SysFont('Calibri', 40, True, False)
        font_1 = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Score: " + str(game.score), True, '#000000')
        text_game_over = font.render("Game Over", True, '#000000')
        text_game_over1 = font.render("Press ESC", True, '#000000')       

        #Ending the game if state is gameover
        screen.blit(text, [300, 0])
        if game.state == "gameover":
            screen.blit(text_game_over, [300, 200])
            screen.blit(text_game_over1, [300, 265])
       
        game.draw_next_block(screen)

        pygame.display.flip()
        clock.tick(fps)     

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris by DataFlair")
run = True
while run:
    screen.fill((16, 57, 34 ))
    font = pygame.font.SysFont("Calibri", 70, bold=True)
    label = font.render("Press any key to begin!", True, '#FFFFFF')

    screen.blit(label, (10, 300 ))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            startGame()
pygame.quit()