import pygame
from constants import *
from pygame import *

pygame.init()
screen = pygame.display.set_mode((width, height))

class Board:
    # constructor for the Board class
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    # draws the outline of the grid + each cell
    def draw(self):
        # to draw the bold lines
        # horizontal
        for i in range(1, big_rows):
            pygame.draw.line(
                screen,
                line_color,
                (0, i * big_square_size),
                (width, i * big_square_size),
                big_line_width

            )
        # vertical
        for j in range(1, big_cols):
            pygame.draw.line(
                screen,
                line_color,
                (j * big_square_size, 0),
                (j * big_square_size, height),
                big_line_width

            )

        # to draw thin lines
        # horizontal
        for x in range(1, small_rows):
            pygame.draw.line(
                screen,
                line_color,
                (0, x * small_square_size),
                (width, x * small_square_size),
                small_line_width

            )
        # vertical
        for y in range(1, small_cols):
            pygame.draw.line(
                screen,
                line_color,
                (y * small_square_size, 0),
                (y * small_square_size, height),
                small_line_width

            )
    # gives the terminal a background color
    screen.fill(bg_color)

    # marks the cell as the current selected cell
    # must select cell before user can edit value or sketched value
    def select(self, row, col):
        selected_cell = self.board[row, col]
        return selected_cell

    # returns tuple of (row, col) if x and y are on the board -if not, returns None
    def click(self, x, y):
        if x <= 540 or y <= 540:
            if x < _
                return (x, y)
        else:
            return None


    # clears value of selected cell -can only remove cell/sketch values from user
    def clear(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.board.set_cell_value(' ')
                screen.fill(bg_color)
                self.board.draw()
                pygame.display.update()

    # sets the sketched value of the selected cell to equal user input
    # will be displayed in top left corner of cell using draw() function
    def sketch(self, value):
        self.update_cells(value)

    def place_number(self, value):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ENTER:
                self.board.set_cell_value(value)
                screen.fill(bg_color)
                self.board.draw()
                pygame.display.update()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
