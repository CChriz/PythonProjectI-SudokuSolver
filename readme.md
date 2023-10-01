# Sudoku Solver

This Python code provides a Sudoku solver that can solve 9x9 Sudoku puzzles. It uses a combination of techniques, including constraint propagation and backtracking, to solve Sudoku puzzles. Here's an overview of the code and its functions:

## Table of Contents
1. [Introduction](#introduction)
2. [Functions](#functions)
3. [Usage](#usage)

## Introduction

This Sudoku solver is implemented in Python and provides a set of functions for solving 9x9 Sudoku puzzles. It includes methods for validating Sudoku boards, reducing possible values in squares, and solving Sudoku puzzles through constraint propagation and backtracking.

## Functions

### `getAffectedSquares(r, c)`
This function returns a list of coordinates for every square affected by a target square at given coordinates `(r, c)`. It combines lists of all squares in the target square's row, column, and block.

### `getBlockStart(coord)`
This function takes a single coordinate and returns the coordinate where the target square's block starts. It's used to determine the starting row and column indexes for the block that contains the target square.

### `isValid(sudoku, coords, value)`
Checks if the target value is valid within its row, column, and block. It returns a Boolean value indicating whether the value is valid.

### `isSudokuValid(sudoku)`
Checks if a Sudoku puzzle is valid by verifying that each value in the puzzle adheres to the rules of Sudoku. It returns a Boolean value indicating whether the Sudoku puzzle is valid.

### `getBlockCoords(r, c)`
This function returns all 9 coordinates within a target square's block. It's used to retrieve the coordinates of all squares within the same block as the target square.

### `copySudoku(sudoku)`
Creates a copy of a new Sudoku board, replacing empty squares with all possible values (1-9). It returns a new 9x9 Sudoku board with possible values instead of blank squares.

### `copyPossibles(possibles)`
Creates a copy of a board of possible values, replacing all uncertain squares with 0 (empty). It returns a new 9x9 Sudoku board without possible values (0 for blank squares).

### `reduce(possibles)`
Iterates through the entire board and looks for squares with confirmed values (only 1 possible value) and removes that value from the possible values of every other square affected by the target square. It returns a Boolean value indicating whether progress has been made.

### `findSingles(possibles)`
Checks if possible values have only appeared once (both possibles and confirmed squares) within rows, columns, and blocks by calling `findSinglesIn`. It returns a Boolean value indicating whether progress has been made.

### `findSinglesIn(possibles, rcb, value)`
Checks through all rows, columns, or blocks if a given value has only appeared once in each. It sets the value of squares that contain the target value as the only possible value (if not already confirmed) and returns a Boolean value indicating whether progress has been made.

### `findBlank(sudoku)`
Checks each square on the Sudoku and returns a set of coordinates upon reaching a blank square. It returns coordinates in the format `(row index, column index)`.

### `reducePossibles(possibles)`
Recursively calls itself to try and logically reduce the possibilities within each square through calling `reduce` and `findSingles`. The process is repeated until no more progress is made.

### `try_solve(sudoku, possibles)`
Tries to solve a Sudoku puzzle and returns its solution (if one exists). It uses backtracking to fill in the Sudoku squares, starting from blank squares. It returns a Boolean value indicating whether the Sudoku is solved.

### `sudoku_solver(sudoku)`
Initiates the solving process of a Sudoku and returns its solution if there is one. It first checks if the starting Sudoku is valid, and if so, it attempts to solve it using various techniques. If a solution is found, it returns the filled Sudoku board. If the Sudoku is not valid or has no solution, it returns a Sudoku board filled with -1 values.

## Usage
To use this Sudoku solver, you can call the `sudoku_solver(sudoku)` function, passing in a 9x9 NumPy array representing the unsolved Sudoku puzzle. The function will return the solved Sudoku puzzle or a Sudoku board filled with -1 values if no solution is found.

### Call the Sudoku solver function to solve the puzzle.
solved_sudoku = sudoku_solver(sudoku_puzzle)
print(solved_sudoku)
