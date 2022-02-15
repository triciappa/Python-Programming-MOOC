def row_correct(sudoku: list, row_no: int):
    for square in sudoku[row_no]:
        if square > 0:
            aux = sudoku[row_no].count(square)
            if aux > 1:
                return False

    return True

def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        aux = row[column_no]
        if aux > 0 and aux in numbers:
            return False
        
        numbers.append(aux)
    
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for i in range (row_no,row_no+3):
        for j in range (column_no,column_no+3):
            if sudoku[i][j] > 0 and  sudoku[i][j] in numbers:
                return False  
            numbers.append(sudoku[i][j])
    return True


def sudoku_grid_correct(sudoku: list):
    row_index = 0
    column_index = 0

    while row_index < len(sudoku):
        check_row = row_correct(sudoku, row_index)
        if check_row == False:
            return False
        row_index += 1

    while column_index < len(sudoku):
        check_column = column_correct(sudoku, column_index)
        if check_column == False:
            return False
        column_index += 1
    
    for i in range (0, 9, 3):
        for j in range (0, 9, 3):
            check_block = block_correct(sudoku, i, j)
            if check_block == False:
                return False

    return True 


if __name__ == "__main__":
    sudoku1 = [
      [9, 0, 0, 0, 8, 0, 3, 0, 0],
      [2, 0, 0, 2, 5, 0, 7, 0, 0],
      [0, 2, 0, 3, 0, 0, 0, 0, 4],
      [2, 9, 4, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 7, 3, 0, 5, 6, 0],
      [7, 0, 5, 0, 6, 0, 4, 0, 0],
      [0, 0, 7, 8, 0, 3, 9, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 3],
      [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))

    sudoku3 = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    print(sudoku_grid_correct(sudoku3))
