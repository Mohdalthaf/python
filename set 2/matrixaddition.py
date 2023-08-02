def matrix_addition(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

  
    result = [[0] * cols for _ in range(rows)]

   
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result


print("Enter elements of Matrix 1:")
rows1 = int(input("Enter the number of rows: "))
cols1 = int(input("Enter the number of columns: "))

matrix1 = []
for i in range(rows1):
    row = []
    for j in range(cols1):
        element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix1.append(row)


print("\nEnter elements of Matrix 2:")
rows2 = int(input("Enter the number of rows: "))
cols2 = int(input("Enter the number of columns: "))

matrix2 = []
for i in range(rows2):
    row = []
    for j in range(cols2):
        element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix2.append(row)


if rows1 != rows2 or cols1 != cols2:
    print("Matrix addition is not possible.")
else:
   
    result_matrix = matrix_addition(matrix1, matrix2)

   
    print("\nMatrix Addition:")
    for row in result_matrix:
        print(row)
