factorial_dict = {}  

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in factorial_dict:
        return factorial_dict[n]
    elif n == 0 or n == 1:
        factorial_dict[n] = 1
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
            factorial_dict[i] = result
        return result

num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}.")
print(factorial_dict)