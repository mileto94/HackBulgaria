def sudoku_solved(sudoku):
    return check_rows(sudoku) and check_colums(sudoku) and check_squares(sudoku)

def check_rows(sudoku):
    number_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    count = 0
    for i in range(9):
        for j in range(9):
            number_dict[sudoku[i][j]] += 1
        if number_dict[sudoku[i][j]] != 1:
            count = 0
        else:
            count += 1
            number_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    if count == 9:
        return True
    else:
        return False

def check_colums(sudoku):
    number_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    count = 0
    for i in range(9):
        for j in range(9):
            number_dict[sudoku[j][i]] += 1
        if number_dict[sudoku[j][i]] != 1:
            count = 0
        else:
            count += 1
            number_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    if count == 9:
        return True
    else:
        return False

def check_squares(sudoku):
    number_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    count = 0
    for index in range(0,9,3):
        for i in range(index,index+3):
            for j in range(index,index+3):
                number_dict[sudoku[j][i]] += 1
            if number_dict[sudoku[j][i]] != 1:
                count = 0
            else:
                count += 1
        if count == 3:
            return True
        else:
            return False

