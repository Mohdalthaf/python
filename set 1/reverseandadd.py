def reverse_number(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    while not is_palindrome(n):
        reverse = reverse_number(n)
        n += reverse
        print(n)
    
    return n

number = int(input("Enter a number: "))
result = reverse_and_add(number)
print("Palindrome sum:", result)
