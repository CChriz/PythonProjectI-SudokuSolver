import numpy as np

# list of coordinates for all 9 rows on the sudoku board
# one row per sublist from top to bottom
rows = [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)],
        [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)],
        [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)],
        [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)],
        [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)],
        [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)],
        [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8)],
        [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)],
        [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]
        ]

# list of coordinates for all 9 columns on the sudoku board
# one column per sublist from left to right
cols = [[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)],
        [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)],
        [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)],
        [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)],
        [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4)],
        [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)],
        [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)],
        [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)],
        [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)]
        ]

# list of coordinates for all 9 blocks on the sudoku board
# one block per sublist from top-left to bottom-right (in a left to right manner)
blocks = [[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
          [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
          [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
          [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
          [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
          [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
          [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
          [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
          [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
          ]


# getAffectedSquares returns a list of coordinates for every square affected by target square at
# given coordinates
# @param : coordinates of target square - format (r, c)
# @return : list of affected squares coordinates
def getAffectedSquares(r, c):
    # returns combined lists of all current row's, column's and block's sqaures' coordinates
    return rows[r] + cols[c] + getBlockCoords(r, c)


# getBlockStart takes a single coordinate and returns the coordinate where
# the target square's block starts
# @param : integer coordinate
# @return : integer starting coordinate of block
def getBlockStart(coord):
    # for indexes 0-2, starting coordinate of block at 0
    if coord < 3:
        return 0
    # for indexes 3-5, starting coordinate of block at 3
    elif coord < 6:
        return 3
    # for others - indexes 6-8, starting coordinate of block at 6
    else:
        return 6
    

# isValid checks if target value is valid within its row, column and block
# @param : current sudoku, the coordinates and value of target square
# @return : Boolean - if value at target square is valid
def isValid(sudoku, coords, value):
    # loop cycles through all values in current row
    for c in range(0, 9):
        # checks if current value is identical to target square's value
        # except if it is the target value itself (same column index)
        if (sudoku[coords[0]][c] == value) and (coords[1] != c):
            return False
    # loop cycles through all values in current column
    for r in range(0, 9):
        # checks if current value is identical to target square's value
        # except if it is the target value itself (same row index)
        if (sudoku[r][coords[1]] == value) and (coords[0] != r):
            return False

    # get starting row and column indexes for current block - by calling getBlockStart
    start_indexes = (getBlockStart(coords[0]), getBlockStart(coords[1]))

    # first loop cycles through the 3 rows within the current block
    for r in range(start_indexes[0], start_indexes[0] + 3):
        # second loop cycles through the 3 values within each row in the block
        for c in range(start_indexes[1], start_indexes[1] + 3):
            # checks if current value is identical to target value
            # except if target value itself (same coordinates)
            if (sudoku[r][c] == value) and (coords != (r, c)):
                return False

    # if passing all checks, return true - value is valid
    return True


# isSudokuValid checks if a sudoku is valid
# @param : target sudoku puzzle (9x9 numpy array)
# @return : whether the sudoku is valid (Boolean)
def isSudokuValid(sudoku):
    # first loop cycles through each row of the board
    for r in range(0, 9):
        # second loop cycles through the value in each column of each row
        for c in range(0, 9):
            value = sudoku[r][c]
            # check if current value is valid unless current value is 0 (empty square)
            # otherwise proceed to check next value on sudoku
            if value != 0:
                # if value is not valid, return False - sudoku invalid
                if not (isValid(sudoku, (r, c), value)):
                    return False

    # return True if every value is valid on sudoku - sudoku valid
    return True


# getBlockCoords returns all 9 coordinates within target square's block
# @param : target square's row and column coordinates - format (r, c)
# @return : list of 9 coordinates within target square's block
def getBlockCoords(r, c):
    # temporary list for storing squares' coordinates within the block
    block_coords = []
    # coordinates of top-left square in target square's block retrieved by getBlockStart
    start_indexes = (getBlockStart(r), getBlockStart(c))
    # first loop cycles through the 3 rows within the current block
    for r in range(start_indexes[0], start_indexes[0] + 3):
        # second loop cycles through the 3 values within each row in the block
        for c in range(start_indexes[1], start_indexes[1] + 3):
            # adding each square's coordinates to block's list of coordinates
            block_coords.append((r, c))
    
    return block_coords


# copySudoku creates a copy of a new sudoku board, replacing empty squares with
# all possible values - (1-9)
# @param : 9x9 target sudoku board with blank squares - numpy array
# @return : 9x9 new copy of sudoku board with possible values instead of blank squares - numpy array
def copySudoku(sudoku):
    # empty new 9x9 numpy array for storing possible values
    possibles = np.empty((9, 9), dtype=object)
    # first loop cycles through each row of the sudoku board
    for r in range(0, 9):
        # second loop cycles through the values in the columns within each row
        for c in range(0, 9):
            # replace any empty square (0) with list of all possible values 1-9
            # otherwise value copied as normal
            if sudoku[r][c] == 0:
                possibles[r][c] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                possibles[r][c] = [sudoku[r][c]]

    return possibles


# copyPossibles creates a copy of a board of possible values, replacing all uncetain squares with 0 (empty)
# @param : 9x9 sudoku board of possible values - numpy array
# @return : 9x9 sudoku board without possible values (0 for blank squares) - numpy array
def copyPossibles(possibles):
    # empty new 9x9 numpy array for processed sudoku board
    new = np.empty((9, 9), dtype=object)
    # first loop cycles through each row of the sudoku board
    for r in range(0,9):
        # second loop cycles through values in the columns within each row
        for c in range(0,9):
            # set new board's current square to that of possibles board if value is confirmed
            # (only one possible value), otherwise set to 0 (empty)
            if len(possibles[r][c]) == 1:
                new[r][c] = possibles[r][c][0]
            else:
                new[r][c] = 0

    return new


# reduce iterates through entire board and looks for squares with confirmed values (only 1 possible value)
# then removes that value from the possible values of every other square affected by the target square
# @param : 9x9 sudoku board of possible values - numpy array
# @return : whether progress has been made - Boolean
def reduce(possibles):
    # set progress made to false at start
    progress = False

    # first loop cycles through each row of the sudoku board
    for r in range(0, 9):
        # second loop cycles through values in each column within every row
        for c in range(0, 9):
            # get confirmed value/possible values of current square
            current_square = possibles[r][c]
            # if current square has confirmed value (only 1 possible value), continue to check if
            # any squares affected by current square contains it within their possible values
            # otherwise move on to repeat check on next square
            if len(current_square) == 1:
                confirmed = current_square[0]
                # list of affected squares' coordinates retrieved by getAffectedSquares
                affectedSquares = getAffectedSquares(r, c)
                # third loop cycles through each of the affeted squares' coordinates
                for next_coord in affectedSquares:
                    # check if affected square being checked contains the value and if it's not the current square
                    # if so, the value will be removed and progress made is set to true
                    if confirmed in possibles[next_coord] and (r, c) != next_coord:
                        possibles[next_coord].remove(confirmed)
                        progress = True
                        
    return progress


# findSingles checks if possible values have only appeared once (both possibles and confirmed squares) within
# a board of possible values - in rows, columns and in blocks - by calling findSinglesIn
# @param : 9x9 sudoku board of possible values - numpy array
# @return : whether progress has been made - Boolean
def findSingles(possibles):
    # set progress made to false before checking
    progress = False
    # loop cycles through all possible values for all rows, columns and blocks (1-9)
    # for each possible value, check if they only have one appearance in every row, column and block
    # by calling findSinglesIn, progress is set to true if any values are changed
    for value in range(1, 10):
        if findSinglesIn(possibles, rows, value):
            progress = True
        if findSinglesIn(possibles, cols, value):
            progress = True
        if findSinglesIn(possibles, blocks, value):
            progress = True
    
    # return if any progress has been made after checking all values in rows, columns and blocks
    return progress


# findSinglesIn checks through all rows, columns or blocks if a given value has only appeared once in each
# if so, set that square's values to the target value then continue to check next square until all is checked
# @param : 9x9 sudoku board of possible values (numpy array), "perspective" - row, column or block, target value
# @return : whether progress has been made - Boolean
def findSinglesIn(possibles, rcb, value):
    # set progress made to false before checking
    progress = False
    # first loop to cycle through every sublist within the rows, columns or blocks
    # (each line = coordinates of 1 row or 1 column or 1 block)
    for line in rcb:
        # number of appearances set to zero before checking each row, column or block
        appearances = 0
        # target square's coordinates is set to None before checking each row, column or block
        target_square = None
        # second loop to cycle through each individual square's coordinates within each sublist
        for coords in line:
            # check if target value is within current square's possible values
            # if so, increment appearances by 1 and set target square to current square's coordinates
            if value in possibles[coords]:
                appearances += 1
                target_square = coords

        # after checking an entire line (row, column or block) check if the target value being checked against
        # has only appeared once and that the target square isn't already confirmed (only 1 possible value)
        # if so - set the value of the square of where target value is found to only the target value itself
        # as there can be no other possible values, and set progress made to true
        if (appearances == 1) and (len(possibles[target_square]) != 1):
            possibles[target_square] = [value]
            progress = True

    # after checking every line (rows, columns or blocks) return whether any progress is made
    return progress


# findBlank checks each square on the sudoku and returns a
# set of coordinates upon reaching a blank square
# @param : target sudoku puzzle (9x9 numpy array)
# @return : coordinates of a blank square in the format(row index, column index)
def findBlank(sudoku):
    # first loop cycles through each row of the board
    for r in range(0, 9):
        # second loop cycles through the value in each column of each row
        for c in range(0, 9):
            # if value at current square is 0 (blank), return coordinates as tuple
            if sudoku[r][c] == 0:
                return r, c
    # return none if no blank squares left
    return None


# reducePossibles recursively calls itself to try and logically reduce the possibilities within each square
# through calling reduce and findSingles, process is repeated until no more progress is made
# @param : 9x9 sudoku board of possible values - numpy array
def reducePossibles(possibles):
    # progress made set to false at the start each time
    progress = False
    # first try to reduce the possible values in each square by calling reduce
    reduce(possibles)
    # then try to find squares where it contains the only possible value within its row, column or block is held
    # by calling findSingles, if found, changes would have been made so progress is set to true
    if findSingles(possibles):
        progress = True

    # if progress is made recursive call until no further process is made
    if progress:
        reducePossibles(possibles)


# try_solve tries to solve a sudoku puzzle and returns its solution
# (if one exists)
# @param : unsolved sudoku puzzle (9x9 numpy array)
# @return : if sudoku is solved (boolean)
def try_solve(sudoku, possibles):
    # try to find a blank square in sudoku
    blank_coords = findBlank(sudoku)
    # when no blank square is found - this means the sudoku has been solved
    if blank_coords is None:
        return True

    # otherwise continue to solve sudoku
    # loop cycles through all possible values for each square
    for value in possibles[blank_coords[0]][blank_coords[1]]:
        # check if current value is valid for target square
        if isValid(sudoku, blank_coords, value):
            # if value is valid, set current square to valid value then
            sudoku[blank_coords[0]][blank_coords[1]] = value
            # recursive call to continue solving upon next blank square
            if try_solve(sudoku, possibles):
                return True
            # otherwise reset square back to blank square
            sudoku[blank_coords[0]][blank_coords[1]] = 0

    # if no solution - no possible values for current blank square
    return False


# sudoku_solver initiates the solving process of a sudoku and returns its
# solution if there is one
# @param : unsolved sudoku puzzle (9x9 numpy array)
# @return : solved sudoku puzzle (9x9 numpy array of integers) OR
# only -1 values only if no solutions found
def sudoku_solver(sudoku):
    # first check if sudoku puzzle given is valid to start with
    if isSudokuValid(sudoku):
        # if sudoku puzzle given is valid, initiate solving process
        # returning the solutions if one exists
        # first create a copy of the current sudoku with possible values instead of 0 (blank squares)
        possibles = copySudoku(sudoku)
        # then try using the board of possible values to reduce the possible values in each square
        reducePossibles(possibles)
        # copy the reduced board back to blank board for solving with backtracking
        sudoku = copyPossibles(possibles)
        # if successfully solved, return filled sudoku board
        if try_solve(sudoku, possibles):
            return sudoku

    # otherwise in the case where the starting sudoku isn't valid OR
    # if there is no solutions to the sudoku puzzle, -1 values are returned
    return np.array([
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    ])


# set array to -1
# raise NotImplementedError()
