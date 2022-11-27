import pygame
import random
import math


class SudokuGenerator:
    # run when class SudokuGenerator is instantiated
    def __init__(self, row_length, removed_cells):
        # initialize row length to be function argument, row_length should always be 9
        self.row_length = row_length
        # FIXME: removed_cells depends on outside information
        self.removed_cells = removed_cells
        # inits box_length as sqrt of row length, used in provided methods
        self.box_length = int(math.sqrt(row_length))

        self.board = []  # initialize self.board to be empty list
        for i in range(9):  # loop 0 to 9 (not inclusive)
            sublist = []  # initialize empty list as sublist
            for j in range(9):  # loop 0 to 8 again
                # add empty string to sublist, once loop is done sublist is an empty row
                sublist.append(0)
            # add sublist to the end of self.board, end with 2D 9x9 list of empty strings
            self.board.append(sublist)

    def get_board(self):  # called to return the board list
        return self.board  # return unformatted board list

    def print_board(self):  # called to print out formatted board
        for sublist in self.board:  # for each sublist in board list...
            for char in sublist:  # for each character in each sublist...
                # print the character and a space, with no newline
                print(char, end=' ')
            else:  # when current loop ends...
                print('')  # print newline

    # called to check whether number is valid to insert into row
    def valid_in_row(self, row, num):
        # checks with row input from 0 to 8 (not 9)
        for char in self.board[row]:
            if num == char:  # if the number ever equals the selected value...
                return False  # returns False because number is already in row and thus not a valid placement
        else:  # if for loop runs through and does not find any equalities...
            return True  # return true because number is a valid input

    # called to check whether number is valid to insert into column
    def valid_in_col(self, col, num):
        for sublist in self.board:  # checks with col input from 0 to 8 (not 9)
            # if the number ever equals the selected number...
            if num == sublist[col]:
                return False  # returns False because number is already in column and thus not a valid placement
        else:  # if for loop runs through and does not find any equalities...
            return True  # return true because number is a valid input

    # called to chec whether number is valid to insert in box
    def valid_in_box(self, row_start, col_start, num):
        for i in range(3):  # iterating i from 0-2
            for j in range(3):  # iterating j from 0-2
                if num == self.board[row_start + i][col_start + j]:
                    # ^^ checks whether num is equal to any value in 3x3 section starting from row_start and col_start
                    return False  # if there are any equalities, returns False because num is not valid in box
            else:  # if there were no errors...
                return True  # return True because number is valid in box

    # calls previous three functions to check whether number placement is valid
    def is_valid(self, row, col, num):
        # we need to check the three previous functions to make sure the position is valid to enter
        # check if given num placement is valid in row
        if not self.valid_in_row(row, num):
            return False  # if it is not, return False
        # check if given num placement is valid in col
        elif not self.valid_in_col(col, num):
            return False  # if it is not, return False
        # check if given num placement is valid in box
        elif not self.valid_in_box((row // 3) * 3, (col // 3) * 3, num):
            # ^^ row_start and col_start are only multiples of three because that is top left corner of box
            return False  # if it is not, return False
        else:  # if all these tests passed...
            return True  # position is valid

    def fill_box(self, row_start, col_start):  # called to fill a box with random values
        unused_in_box = []  # initialize empty list unused_in_box, soon to be filled
        for i in range(9):  # increment through 0-8
            unused_in_box.append(i)  # add int from 0-8 into unused_in_box list

        for i in range(3):  # iterating i from 0-2
            for j in range(3):  # iterating j from 0-2
                # generate random number from 1 - 9
                rand_int = random.randint(0, 8)
                while True:  # loop until broken
                    if rand_int in unused_in_box:  # if the rand_int has not been used yet...
                        # add rand_int to corresponding pos
                        self.board[row_start + i][col_start + j] = rand_int + 1
                        # remove rand_int from unused_in_box
                        unused_in_box.remove(rand_int)
                        break  # end loop
                    else:  # if int has been used...
                        # add 1 to rand_int mod 9 and try again
                        rand_int = (rand_int + 1) % 9

        # results in a 3x3 area of board filled with 9 unique ints from 1-9 randomized in square

    def fill_diagonal(self):  # called in board generation
        for i in range(3):  # iterate only three times
            # fills diagonal boxes with three random sets of numbers
            self.fill_box(i * 3, i * 3)

    def fill_remaining(self, row, col):  # function provided, not sure how it works
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):  # called to fill solution to board
        # first fill three diagonal boxes with random numbers...
        self.fill_diagonal()
        # then finish with filling the remaining squares
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):  # called to remove cells from board
        # initialize removed_list as empty list, this list records all removed positions
        removed_list = []
        # iterating over the number of removed cells, determined by difficulty
        for i in range(self.removed_cells):
            # row is decided by random integer from 0-8
            row = random.randint(0, 8)
            # col is decided also by random int from 0-8
            col = random.randint(0, 8)
            # if these coords are not in the list of removed positions...
            if [row, col] not in removed_list:
                self.board[row][col] = 0  # set that position to zero
                # add that position to the list
                removed_list.append([row, col])


def generate_sudoku(size, removed):  # called to generate a full board ready for gameplay
    # instantiate SudokuGenerator with specified size and num of removed cells
    board = SudokuGenerator(size, removed)
    board.fill_values()  # calls fill_values() function to fill board with random numbers
    board.remove_cells()  # remove random cells to initialize game

    return board  # return the board instance


board = generate_sudoku(9, 30)  # test case
board.print_board()  # test case


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
