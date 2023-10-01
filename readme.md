# Sudoku Solver

This Python code provides a Sudoku solver that can solve 9x9 Sudoku puzzles. It uses a combination of techniques, including constraint propagation and backtracking, to solve Sudoku puzzles. Here's an overview of the code and its functions:

## Table of Contents
1. [Introduction](#introduction)
2. [Functions](#functions)
3. [Usage](#usage)
4. [License](#license)

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
Checks if a Sudoku puzzle is valid by verifying that each value in the puzzle adheres to the rules of Sudoku. It returns a Boolean value indicating
