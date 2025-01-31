
# Arithmetic Operations in Python

This document explains how to perform arithmetic operations in Python. It covers basic operations like addition, subtraction, multiplication, and division, as well as advanced operations like modulus, exponentiation, and mathematical functions.

---

## Key Concepts

### 1. **Basic Arithmetic Operations**
Python supports the following basic arithmetic operations:

| Operator | Description          | Example           | Result |
|----------|----------------------|-------------------|--------|
| `+`      | Addition             | `5 + 3`           | `8`    |
| `-`      | Subtraction          | `10 - 4`          | `6`    |
| `*`      | Multiplication       | `7 * 2`           | `14`   |
| `/`      | Division             | `15 / 3`          | `5.0`  |
| `//`     | Floor Division       | `15 // 2`         | `7`    |
| `%`      | Modulus (Remainder)  | `10 % 3`          | `1`    |
| `**`     | Exponentiation       | `2 ** 3`          | `8`    |

#### Examples
```python
# Addition
print(5 + 3)  # Output: 8

# Subtraction
print(10 - 4)  # Output: 6

# Multiplication
print(7 * 2)  # Output: 14

# Division
print(15 / 3)  # Output: 5.0

# Floor Division
print(15 // 2)  # Output: 7

# Modulus
print(10 % 3)  # Output: 1

# Exponentiation
print(2 ** 3)  # Output: 8
```

---

### 2. **Advanced Arithmetic Operations**
Python also supports more advanced arithmetic operations, such as:

#### **Modulus (`%`)**
   - Returns the remainder of a division.
   ```python
   print(10 % 3)  # Output: 1
   ```

#### **Exponentiation (`**`)**
   - Raises a number to the power of another.
   ```python
   print(2 ** 3)  # Output: 8
   ```

#### **Compound Assignment Operators**
   - Combine arithmetic operations with assignment.
   ```python
   x = 5
   x += 3  # Equivalent to x = x + 3
   print(x)  # Output: 8
   ```

---

### 3. **Mathematical Functions**
Python provides a variety of built-in mathematical functions through the `math` module. Some of the most commonly used functions are:

#### **Using the `math` Module**
   - Import the `math` module to access advanced mathematical functions.
   ```python
   import math
   ```

#### **Common Functions**
   - `math.sqrt(x)`: Returns the square root of `x`.
     ```python
     print(math.sqrt(16))  # Output: 4.0
     ```
   - `math.pow(x, y)`: Returns `x` raised to the power of `y`.
     ```python
     print(math.pow(2, 3))  # Output: 8.0
     ```
   - `math.floor(x)`: Rounds `x` down to the nearest integer.
     ```python
     print(math.floor(3.7))  # Output: 3
     ```
   - `math.ceil(x)`: Rounds `x` up to the nearest integer.
     ```python
     print(math.ceil(3.2))  # Output: 4
     ```
   - `math.pi`: Returns the value of π (pi).
     ```python
     print(math.pi)  # Output: 3.141592653589793
     ```

#### **Rounding Numbers**
   - Use the `round()` function to round a number to the nearest integer or a specified number of decimal places.
   ```python
   print(round(3.14159, 2))  # Output: 3.14
   ```

---

### 4. **Practical Examples**

#### **Example 1: Calculating the Area of a Circle**
   ```python
   import math

   radius = float(input("Enter the radius of the circle: "))
   area = math.pi * (radius ** 2)
   print(f"The area of the circle is: {round(area, 2)}")
   ```

#### **Example 2: Compound Interest Calculation**
   ```python
   principal = float(input("Enter the principal amount: "))
   rate = float(input("Enter the annual interest rate (in %): ")) / 100
   time = float(input("Enter the time period (in years): "))

   amount = principal * (1 + rate) ** time
   print(f"The final amount after {time} years is: {round(amount, 2)}")
   ```

---

## Conclusion
Arithmetic operations are fundamental to programming in Python. Whether you're performing basic calculations or advanced mathematical operations, Python provides a wide range of tools and functions to help you achieve your goals.

---

### Additional Resources
- [Python Math Module Documentation](https://docs.python.org/3/library/math.html)
- [Real Python: Numbers and Math](https://realpython.com/python-numbers/)

---

This `Arithmetic-Operations.md` file provides a comprehensive guide to arithmetic operations in Python, complete with examples and practical use cases. It’s ready to be added to your GitHub repository!
