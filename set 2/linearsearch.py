def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
numbers = [5, 2, 8, 10, 3, 7]
print(numbers)
target_number = int(input("Enter the number to search: "))

index = linear_search(numbers, target_number)

if index != -1:
    print(f"The number {target_number} is found at index {index}.")
else:
    print(f"The number {target_number} is not found in the list.")
