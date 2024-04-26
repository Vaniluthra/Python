'''
Description
Program to rotate a given matrix by 90 degrees
'''
def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return matrix

m = int(input())
n = int(input())

matrix = []
for i in range(m):
    row = list(map(int, input().split()))
    if len(row) != n:
        print("Error: Number of elements in each row should be equal to the number of columns.")
        exit()
    matrix.append(row)

rotated_matrix = rotate_matrix(matrix)
for row in rotated_matrix:
    print(row)
