# Requirements:

# The function print_sudoku(sudoku: list) takes a two-dimensional 
# array representing a sudoku grid as its argument. The function 
# should print out the grid in the format specified in the examples below.

# The function add_number(sudoku: list, row_no: int, column_no: int, number:int) 
# takes a two-dimensional array representing a sudoku grid, two integers referring 
# to the row and column indexes of a single square, and a single digit between 1 
# and 9, as its arguments. The function should add the digit to the specified 
# location in the grid.

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


def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku [row_no][column_no] = number
    

if __name__ == "__main__":
    sudoku  = [
        [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
        [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
        [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
        [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
        [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
        [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
        [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
        [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
        [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
