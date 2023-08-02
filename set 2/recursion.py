def print_numbers(n):
    if n < 0:
        return
    print(n)
    print_numbers(n-1)

num = int(input("Enter a number: "))
print("Numbers from", num, "to 0:")
print_numbers(num)