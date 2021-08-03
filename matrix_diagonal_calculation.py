# Given a quadratic matrix, write a method to calculate the sum of the main and secondary diagonals

def calculate_diagonal(matrix):
    """Method to calculate the sum of the main and secondary diagonal"""
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    matrix_length = len(matrix)
    for i in range(matrix_length):
        main_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][matrix_length-i-1]
    print("The main diagonal sum is {0} and the secondary "
          "diagonal sum is {1}".format(main_diagonal_sum, secondary_diagonal_sum))


given_matrix = [
    [20, -2, 172],
    [-12, 90, 45],
    [-9, 88, -23]]

try:
    calculate_diagonal(given_matrix)
except IndexError:
    print("The matrix is not quadratic")
else:
    pass