def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        return None

    
    result = [[0] * cols2 for _ in range(rows1)]

 
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

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


if cols1 != rows2:
    print("Matrix multiplication is not possible.")
else:
    result_matrix = matrix_multiplication(matrix1, matrix2)
    print("\nMatrix Multiplication:")
    for row in result_matrix:
        print(row)
