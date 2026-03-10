import math

try:
    num = float(input("Enter a number: "))

    # Calculations using math module
    square_root = math.sqrt(num)
    natural_log = math.log(num)
    sine_value = math.sin(num)

    # Display results
    print("\nResults:")
    print("Square root:", square_root)
    print("Natural logarithm (log base e):", natural_log)
    print("Sine of the number (in radians):", sine_value)

except ValueError:
    print("Please enter a valid number.")
except Exception as e:
    print("An error occurred:", e)