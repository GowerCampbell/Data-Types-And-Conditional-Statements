# Data Type & Conditions Task 2 Written by Gower Campbell.

# Objective: To build confidence and understanding of basic arithmetic operations and user interactions.

# ************ Step 1 ************
# i: Ask the user to enter three different integers.

print('''\nWelcome to Using ARITHMETIC OPERATORS & FUNCTIONS
      Please enter three different integers''')

# Prompt the user to input three different integers
num1 = int(input("\nEnter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Ensure the user enters three different integers
if num1 == num2 or num2 == num3 or num1 == num3:
    print("Please enter three different integers.")
    exit()  # Exit the program if the input is invalid

# Import the math module for advanced mathematical operations
import math

# ************ Step 2 ************
# ii: Perform and print out the following calculations:

# The sum of all numbers together
total = num1 + num2 + num3
print(f"\nThe total of {num1}, {num2}, and {num3} is: {total}")

# The first number minus the second number
subtract_result = num1 - num2
print(f"\nIf {num1} subtracts {num2}, the result is: {subtract_result}")

# The third number multiplied by the first number
multiplication_result = num3 * num1
print(f"\nIf {num3} multiplies {num1}, the result is: {multiplication_result}")

# The sum of all three numbers divided by the third number
division_result = (num1 + num2 + num3) / num3
print(f"\nIf {num3} divides {num1 + num2 + num3}, the result is rounded up: {math.ceil(division_result)}")

# Here I learned how to work with numbers and user inputs. Code well!
