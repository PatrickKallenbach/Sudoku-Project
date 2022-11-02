import random, math


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):  # run when class SudokuGenerator is instantiated
        self.row_length = row_length  # initialize row length to be function argument, row_length should always be 9
        self.removed_cells = removed_cells  # FIXME: removed_cells depends on outside information
        self.box_length = int(math.sqrt(row_length))  # inits box_length as sqrt of row length, used in provided methods

        self.board = []  # initialize self.board to be empty list
        for i in range(9):  # loop 0 to 9 (not inclusive)
            sublist = []  # initialize empty list as sublist
            for j in range(9):  # loop 0 to 8 again
                sublist.append(0)  # add empty string to sublist, once loop is done sublist is an empty row
            self.board.append(sublist)  # add sublist to the end of self.board, end with 2D 9x9 list of empty strings

    def get_board(self):  # called to return the board list
        return self.board  # return unformatted board list

    def print_board(self):  # called to print out formatted board
        for sublist in self.board:  # for each sublist in board list...
            for char in sublist:  # for each character in each sublist...
                print(char, end=' ')  # print the character and a space, with no newline
            else:  # when current loop ends...
                print('')  # print newline

    def valid_in_row(self, row, num):  # called to check whether number is valid to insert into row
        for char in self.board[row]: # checks with row input from 0 to 8 (not 9)
            if num == char:  # if the number ever equals the selected value...
                return False  # returns False because number is already in row and thus not a valid placement
        else:  # if for loop runs through and does not find any equalities...
            return True  # return true because number is a valid input

    def valid_in_col(self, col, num):  # called to check whether number is valid to insert into column
        for sublist in self.board: # checks with col input from 0 to 8 (not 9)
            if num == sublist[col]:  # if the number ever equals the selected number...
                return False  # returns False because number is already in column and thus not a valid placement
        else:  # if for loop runs through and does not find any equalities...
            return True  # return true because number is a valid input

    def valid_in_box(self, row_start, col_start, num):  # called to chec whether number is valid to insert in box
        for i in range(3):  # iterating i from 0-2
            for j in range(3):  # iterating j from 0-2
                if num == self.board[row_start + i][col_start + j]:
                    # ^^ checks whether num is equal to any value in 3x3 section starting from row_start and col_start
                    return False  # if there are any equalities, returns False because num is not valid in box
            else:  # if there were no errors...
                return True  # return True because number is valid in box

    def is_valid(self, row, col, num):  # calls previous three functions to check whether number placement is valid
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

    def fill_box(self, row_start, col_start):  # called to fill a box with random values
        unused_in_box = []  # initialize empty list unused_in_box, soon to be filled
        for i in range(9):  # increment through 0-8
            unused_in_box.append(i)  # add int from 0-8 into unused_in_box list

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

        # results in a 3x3 area of board filled with 9 unique ints from 1-9 randomized in square

    def fill_diagonal(self):  # called in board generation
        for i in range(3):  # iterate only three times
            self.fill_box(i * 3, i * 3)  # fills diagonal boxes with three random sets of numbers

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
        self.fill_diagonal()  # first fill three diagonal boxes with random numbers...
        self.fill_remaining(0, self.box_length)  # then finish with filling the remaining squares

    def remove_cells(self):  # called to remove cells from board
        removed_list = []  # initialize removed_list as empty list, this list records all removed positions
        for i in range(self.removed_cells):  # iterating over the number of removed cells, determined by difficulty
            row = random.randint(0, 8)  # row is decided by random integer from 0-8
            col = random.randint(0, 8)  # col is decided also by random int from 0-8
            if [row, col] not in removed_list:  # if these coords are not in the list of removed positions...
                self.board[row][col] = 0  # set that position to zero
                removed_list.append([row, col])  # add that position to the list


def generate_sudoku(size, removed):  # called to generate a full board ready for gameplay
    board = SudokuGenerator(size, removed)  # instantiate SudokuGenerator with specified size and num of removed cells
    board.fill_values()  # calls fill_values() function to fill board with random numbers
    board.remove_cells()  # remove random cells to initialize game

    return board  # return the board instance


board = generate_sudoku(9, 30)  # test case
board.print_board()  # test case