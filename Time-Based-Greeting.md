# Time-Based Greeting in Python

This document explains how to create a program that provides a greeting based on the time of day. The program uses user input, conditional statements, and logical operators to determine the appropriate greeting.

---

## Key Concepts

### 1. **Program Overview**
The program asks the user to input the current hour (in 24-hour format) and provides a greeting based on the following criteria:
- **Good Morning**: If the hour is less than 12.
- **Good Afternoon**: If the hour is between 12 and 18.
- **Good Evening**: If the hour is 18 or later.

---

### 2. **Steps to Build the Program**

#### Step 1: Collect User Input
Use the `input()` function to collect the current hour from the user. Convert the input to an integer for comparisons.

```python
hour = int(input("Enter the current hour (0-23): "))
```

#### Step 2: Determine the Greeting
Use conditional statements (`if`, `elif`, `else`) to determine the appropriate greeting based on the hour.

```python
if hour < 12:
    greeting = "Good Morning!"
elif hour < 18:
    greeting = "Good Afternoon!"
else:
    greeting = "Good Evening!"
```

#### Step 3: Display the Greeting
Print the greeting to the user.

```python
print(greeting)
```

---

### 3. **Complete Program**

```python
# Time-Based Greeting Program

# Step 1: Collect User Input
hour = int(input("Enter the current hour (0-23): "))

# Step 2: Determine the Greeting
if hour < 12:
    greeting = "Good Morning!"
elif hour < 18:
    greeting = "Good Afternoon!"
else:
    greeting = "Good Evening!"

# Step 3: Display the Greeting
print(greeting)
```

---

### 4. **Example Output**

#### Example 1:
```
Enter the current hour (0-23): 9
Good Morning!
```

#### Example 2:
```
Enter the current hour (0-23): 14
Good Afternoon!
```

#### Example 3:
```
Enter the current hour (0-23): 20
Good Evening!
```

---

## Additional Concepts

### 1. **Data Types in Python**
Python supports various numeric data types, including:
- **Integers**: Whole numbers, positive or negative.
  ```python
  hour = 18  # Integer
  ```
- **Floats**: Decimal numbers or numbers with a fractional component.
  ```python
  temperature = 22.5  # Float
  ```

### 2. **Casting Between Numeric Data Types**
You can convert between data types using functions like `int()`, `float()`, and `complex()`.
```python
hour = int(input("Enter the current hour (0-23): "))
```

### 3. **Conditional Statements**
Conditional statements allow you to control the flow of your program based on certain conditions.
```python
if hour < 12:
    greeting = "Good Morning!"
elif hour < 18:
    greeting = "Good Afternoon!"
else:
    greeting = "Good Evening!"
```

### 4. **Logical Operators**
Logical operators are used to combine multiple conditions.
```python
if (hour >= 0) and (hour < 12):
    greeting = "Good Morning!"
elif (hour >= 12) and (hour < 18):
    greeting = "Good Afternoon!"
else:
    greeting = "Good Evening!"
```

---

## Conclusion
The Time-Based Greeting program demonstrates how to use user input, conditional statements, and logical operators to create a dynamic and interactive Python program. It’s a great example of how Python can be used to solve real-world problems.

---

### Additional Resources
- [Python Documentation: Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python: Conditional Statements](https://realpython.com/python-conditional-statements/)


