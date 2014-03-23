def magic_square(matrix):
    sum_rows = 0
    sum_colums = 0
    sum_forward_diag = 0
    sum_backward_diag = 0
    for i in range(len(matrix)):
        sum_rows = sum(matrix[i])

        for j in range(len(matrix)):
            sum_colums += matrix[j][i]

            if i == j:
                sum_forward_diag += matrix[i][j]

            if i + j == len(matrix) - 1:
                sum_backward_diag += matrix[i][j]

    sum_colums = sum_colums // len(matrix)

    if sum_colums == sum_rows and sum_colums == sum_forward_diag and sum_rows == sum_backward_diag:
        return True
    else:
        return False




