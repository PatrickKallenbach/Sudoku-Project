import random, math


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length  # initialize row length to be function argument, row_length should always be 9
        self.removed_cells = removed_cells  # FIXME: removed_cells depends on outside information
        self.box_length = int(math.sqrt(row_length))

        self.board = []  # initialize self.board to be empty list
        for i in range(9):  # loop 0 to 9 (not inclusive)
            sublist = []  # initialize empty list as sublist
            for j in range(9):  # loop 0 to 8 again
                sublist.append(0)  # add empty string to sublist, once loop is done sublist is an empty row
            self.board.append(sublist)  # add sublist to the end of self.board, end with 2D 9x9 list of empty strings

    def get_board(self):
        return self.board

    def print_board(self):
        for sublist in self.board:
            for char in sublist:
                print(char, end=' ')
            else:
                print('')

    def valid_in_row(self, row, num):
        for char in self.board[row]: # checks with row input from 0 to 8 (not 9)
            if num == char:  # if the number ever equals the selected value...
                return False  # returns False because number is already in row and thus not a valid placement
        else:  # if for loop runs through and does not find any equalities...
            return True  # return true because number is a valid input

    def valid_in_col(self, col, num):
        for sublist in self.board: # checks with col input from 0 to 8 (not 9)
            if num == sublist[col]:  # if the number ever equals the selected number...
                return False  # returns False because number is already in column and thus not a valid placement
        else:  # if for loop runs through and does not find any equalities...
            return True  # return true because number is a valid input

    def valid_in_box(self, row_start, col_start, num):
        for i in range(3):  # iterating i from 0-2
            for j in range(3):  # iterating j from 0-2
                if num == self.board[row_start + i][col_start + j]:
                    # ^^ checks whether num is equal to any value in 3x3 section starting from row_start and col_start
                    return False  # if there are any equalities, returns False because num is not valid in box
            else:  # if there were no errors...
                return True  # return True because number is valid in box

    def is_valid(self, row, col, num):
        # we need to check the three previous functions to make sure the position is valid to enter
        if not self.valid_in_row(row, num):  # check if given num placement is valid in row
            return False  # if it is not, return False
        elif not self.valid_in_col(col, num):  # check if given num placement is valid in col
            return False  # if it is not, return False
        elif not self.valid_in_box((row // 3) * 3, (col // 3) * 3, num):  # check if given num placement is valid in box
            # ^^ row_start and col_start are only multiples of three because that is top left corner of box
            return False  # if it is not, return False
        else:  # if all these tests passed...
            return True  # position is valid

    def fill_box(self, row_start, col_start):
        unused_in_box = []
        for i in range(9):
            unused_in_box.append(i)

        for i in range(3):  # iterating i from 0-2
            for j in range(3):  # iterating j from 0-2
                rand_int = random.randint(0, 8)  # generate random number from 1 - 9
                while True:  # loop until broken
                    if rand_int in unused_in_box:  # if the rand_int has not been used yet...
                        self.board[row_start + i][col_start + j] = rand_int + 1  # add rand_int to corresponding pos
                        unused_in_box.remove(rand_int)  # remove rand_int from unused_in_box
                        break  # end loop
                    else:  # if int has been used...
                        rand_int = (rand_int + 1) % 9  # add 1 to rand_int mod 9 and try again

        # results in a 3x3 area of board filled

    def fill_diagonal(self):
        for i in range(3):  # iterate only three times
            self.fill_box(i * 3, i * 3)  # fills diagonal boxes with three random sets of numbers

    def fill_remaining(self, row, col):
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

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        removed_list = []
        for i in range(self.removed_cells):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if [row, col] not in removed_list:
                self.board[row][col] = 0
                removed_list.append([row, col])


def generate_sudoku(size, removed):
    board = SudokuGenerator(size, removed)
    board.fill_values()
    board.remove_cells()

    return board


board = generate_sudoku(9, 30)
board.print_board()