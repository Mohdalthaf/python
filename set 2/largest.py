def find_largest_number(numbers):
    if len(numbers) == 0:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


numbers = [5, 2, 8, 10, 3, 7]

largest_num = find_largest_number(numbers)
print("numbers:",numbers)

if largest_num is not None:
    print("Largest number:", largest_num)
else:
    print("The list is empty.")
