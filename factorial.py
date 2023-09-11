def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
n = 5  # Replace with the number for which you want to calculate the factorial
result = factorial(n)
print(f"The factorial of {n} is {result}")
