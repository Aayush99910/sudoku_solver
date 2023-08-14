import numpy as np

grid = [
    [5, 0, 0, 3, 0, 0, 1, 6, 0],
    [0, 0, 4, 0, 9, 8, 0, 5, 3],
    [0, 2, 7, 0, 0, 1, 4, 0, 9],
    [0, 6, 0, 0, 0, 7, 0, 4, 0],
    [7, 0, 1, 0, 8, 2, 6, 0, 0],
    [0, 3, 8, 0, 6, 0, 9, 0, 2],
    [0, 0, 0, 2, 4, 0, 5, 0, 8],
    [8, 4, 0, 5, 0, 0, 0, 1, 0],
    [9, 5, 6, 0, 0, 3, 7, 0, 0]
]

''' 
This function checks if a number can be put in a cell or not. 
It will check every row and the column and also the subgrid before putting the number
'''
def valid_cell(row, column, number):
    global grid # making the grid global so it can be accessed here
    
    # checking if the number doesn't show in the row
    for i in range(0, 9):
        if (grid[row][i] == number):
            return False
    
    # checking if the number doesn't show in the column
    for i in range(0, 9):
        if (grid[i][column] == number):
            return False
    
    # checking if the number doesn't show in the smaller grid
    row_of_small_grid = (row // 3) * 3
    column_of_small_grid = (column // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if (grid[row_of_small_grid + i][column_of_small_grid + j] == number):
                return False
            
    
    return True # returning true if the number is not present in any of the row, column or subgrid


'''
This function solves the sudoku by going through all the rows and column.
It will also call the valid_cell function to check whether that number will fit in that particular
cell or not. Then we call the function again to fill the rest squares. If it is not possible 
it will return and then reverse the number back to zero and then continue again.
'''
def solve_sudoku():
    global grid
    
    for row in range(0, 9):
        for column in range(0, 9):
            if (grid[row][column] == 0):
                for number in range(1, 10):
                    if (valid_cell(row, column, number)):
                        grid[row][column] = number
                        solve_sudoku()
                        grid[row][column] = 0
                return 
    
    print(np.matrix(grid)) # printing the final result
    
solve_sudoku()       