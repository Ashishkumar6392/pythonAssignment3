def factorial(n):
    """Calculate factorial of n using recursion"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

try:
    num = int(input("Enter a number to calculate factorial: "))
    
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print("Factorial of", num, "is", result)

except ValueError:
    print("Please enter a valid integer.")