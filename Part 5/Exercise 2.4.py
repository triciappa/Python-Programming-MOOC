# Requirements:

# Make a new function call copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) similar
# to the fucntion add_number but in this exercise the function should not change the original grid 
# received as a parameter.


import copy

def print_sudoku(sudoku: list):
    for i in range (9):
        for j in range (9):
            square = sudoku[i][j]
            if square > 0:
                print(f"{square} ", end="")
            else:
                print("_ ", end="")
            
            # We calculate when the column is 3 or 6 to print a space
            if (j + 1) % 3 == 0 and (j + 1) != 9:
                print(end=" ")
        
        # We calculate when the row is 3 or 6 to print a space
        if (i + 1) % 3 == 0:
            print("\n", end="")
        
        print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = copy.deepcopy(sudoku)
    new_sudoku [row_no][column_no] = number
    return new_sudoku

# Course solution:
# def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
#     new_list = []
#     for r in sudoku:
#         new_list.append(r[:])
 
#     new_list[row_no][column_no] = number
#     return new_list


if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
