# Program to find the transpose of a 2x3 matrix

matrix = [[1, 2, 3],
          [4, 5, 6]]

transpose = []

for column in range(3):
    new_row = []
    for row in range(2):
        new_row.append(matrix[row][column])
    transpose.append(new_row)

print("Original matrix:")
for row in matrix:
    print(row)

print("Transpose:")
for row in transpose:
    print(row)
