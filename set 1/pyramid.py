rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Print spaces in each row
    for j in range(1, rows - i + 1):
        print(" ", end="")
    
    # Print numbers in ascending order
    for j in range(1, i + 1):
        print(j, end="")
    
    # Print numbers in descending order
    for j in range(i - 1, 0, -1):
        print(j, end="")
    
    # Move to the next line
    print()