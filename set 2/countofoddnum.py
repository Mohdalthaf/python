def find_odd_numbers(arr):
    odd_numbers = []
    for num in arr:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers


numbers = [2, 5, 8, 11, 14, 17, 20]
print("array:",numbers)
odd_nums = find_odd_numbers(numbers)

print("Odd numbers in the array:")
print(odd_nums)
