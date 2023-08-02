def sum_of_numbers(numbers):
    return sum(numbers)

n = int(input("Enter the count of numbers: "))
numbers = []

for i in range(n):
    number = float(input("Enter a number: "))
    numbers.append(number)

total_sum = sum_of_numbers(numbers)
print("Sum of the numbers:", total_sum)