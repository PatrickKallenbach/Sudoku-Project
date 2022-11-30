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
        self.x = 25 + self.col * self.width
        self.y = 25 + self.row * self.height
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

        # text = self.font.render(str(self.value), 1, (0, 0, 0))
        # self.screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.width, self.height), 3)
        else:
            pygame.draw.rect(self.screen, (0, 0, 0),
                             (self.x, self.y, self.width, self.height), 3)
        if self.value != 0:
            text = self.font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (self.x + 15, self.y + 15))

        # pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)
