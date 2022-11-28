import pygame
import random
import math
from sudoku_generator import SudokuGenerator

class Cell:
    # this class represents a single cell in the sudoku board. There are 81 cells in a board

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.width = 50
        self.height = 50
        self.x = 50 + self.col * self.width
        self.y = 50 + self.row * self.height
        self.selected = False
        self.font = pygame.font.SysFont("comicsans", 40)
        self.sketched = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value
        self.sketched = True

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (self.x, self.y, self.width, self.height), 1)
        if self.value != 0:
            # text = self.font.render(str(self.value), 1, (0, 0, 0))
            # self.screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            if self.selected:
                pygame.draw.rect(self.screen, (255, 0, 0),
                                 (self.x, self.y, self.width, self.height), 3)
            else:
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 (self.x, self.y, self.width, self.height), 3)
            text = self.font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (self.x + 15, self.y + 15))
        else:
            pygame.draw.rect(self.screen, (0, 0, 0),
                             (self.x, self.y, self.width, self.height), 3)


screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Sudoku")
# font = pygame.font.SysFont("comicsans", 40)
# board = generate_sudoku(9, 30)
pygame.init()
pygame.font.init()

cells = []
for i in range(9):
    for j in range(9):
        cells.append(Cell(board.board[i][j], i, j, screen))

run = True
while run:
    # clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for cell in cells:
                if cell.x < pos[0] < cell.x + cell.width and cell.y < pos[1] < cell.y + cell.height:
                    cell.selected = True
                else:
                    cell.selected = False

    screen.fill((255, 255, 255))

    for cell in cells:
        cell.draw()

    pygame.display.update()