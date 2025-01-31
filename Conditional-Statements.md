# Conditional Statements in Python

This document explains how to use conditional statements in Python. It covers `if`, `elif`, and `else` statements, comparison operators, logical operators, and practical examples.

---

## Key Concepts

### 1. **Conditional Statements**
Conditional statements allow you to control the flow of your program based on certain conditions. The main types of conditional statements in Python are:

- **`if` Statement**: Executes a block of code if a condition is `True`.
- **`elif` Statement**: Checks additional conditions if the previous conditions are `False`.
- **`else` Statement**: Executes a block of code if all previous conditions are `False`.

#### Syntax
```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
else:
    # Code to execute if all conditions are False
```

#### Example
```python
num = 10

if num < 12:
    print("The variable num is lower than 12")
elif num > 13:
    print("The variable num is higher than 13")
else:
    print("The variable num is 13")
```

---

### 2. **Comparison Operators**
Comparison operators are used to compare values or variables. They return `True` or `False` based on the condition.

| Operator | Description                  | Example           | Result  |
|----------|------------------------------|-------------------|---------|
| `==`     | Equal to                     | `5 == 5`          | `True`  |
| `!=`     | Not equal to                 | `5 != 3`          | `True`  |
| `>`      | Greater than                 | `10 > 5`          | `True`  |
| `<`      | Less than                    | `10 < 5`          | `False` |
| `>=`     | Greater than or equal to     | `10 >= 10`        | `True`  |
| `<=`     | Less than or equal to        | `10 <= 5`         | `False` |

#### Example
```python
num1 = 10
num2 = 20

if num1 > num2:
    print("num1 is greater than num2")
else:
    print("num1 is not greater than num2")
```

---

### 3. **Logical Operators**
Logical operators are used to combine multiple conditions. They are often used with `if` statements.

| Operator | Description                  | Example                          | Result  |
|----------|------------------------------|----------------------------------|---------|
| `and`    | Both conditions must be True | `(5 > 3) and (10 < 20)`          | `True`  |
| `or`     | At least one condition must be True | `(5 > 3) or (10 > 20)` | `True`  |
| `not`    | Inverts the condition        | `not (5 > 3)`                    | `False` |

#### Example
```python
team1_score = 3
team2_score = 2
game = "over"

if (team1_score > team2_score) and (game == "over"):
    print("Congratulations Team 1, you have won the match!")
else:
    print("Congratulations Team 2, you have won the match!")
```

---

### 4. **Nested Conditional Statements**
You can nest conditional statements inside one another to handle more complex logic.

#### Example
```python
num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")
```

---

### 5. **Practical Examples**

#### Example 1: Time-Based Greeting
```python
hour = int(input("Enter the current hour (0-23): "))

if hour < 12:
    greeting = "Good morning!"
elif hour < 18:
    greeting = "Good afternoon!"
else:
    greeting = "Good evening!"

print(greeting)
```

#### Example 2: Grade Calculator
```python
score = float(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
```

#### Example 3: Traffic Fine System
```python
speed = int(input("Enter your speed (km/h): "))
belt = input("Are you wearing a seatbelt? (yes/no): ").lower()

if (speed > 80) or (belt != "yes"):
    print("Sorry, you have been fined.")
else:
    print("You are driving safely. Keep it up!")
```

---

### 6. **Assignment Operators**
Assignment operators are used to assign values to variables. They can also perform arithmetic operations during assignment.

| Operator | Description                  | Example           | Equivalent |
|----------|------------------------------|-------------------|------------|
| `=`      | Assigns a value              | `x = 5`           | `x = 5`    |
| `+=`     | Adds and assigns             | `x += 3`          | `x = x + 3`|
| `-=`     | Subtracts and assigns        | `x -= 2`          | `x = x - 2`|
| `*=`     | Multiplies and assigns       | `x *= 4`          | `x = x * 4`|
| `/=`     | Divides and assigns          | `x /= 2`          | `x = x / 2`|

#### Example
```python
x = 10
x += 5  # Equivalent to x = x + 5
print(x)  # Output: 15
```

---

## Conclusion
Conditional statements are essential for controlling the flow of your program based on specific conditions. By mastering `if`, `elif`, `else`, and logical operators, you can create dynamic and responsive programs.

---

### Additional Resources
- [Python Documentation: Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python: Conditional Statements](https://realpython.com/python-conditional-statements/)

