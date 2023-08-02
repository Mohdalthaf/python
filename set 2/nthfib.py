def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the value of N: "))

nth_term = fibonacci(n)

if nth_term is not None:
    print(f"The {n}th term in the Fibonacci series is: {nth_term}")
else:
    print("Invalid value of N.")
