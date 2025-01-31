# Triathlon Award Program in Python

This document explains how to create a program that calculates the total time taken to complete a triathlon and awards participants based on their performance. The program uses user input, arithmetic operations, and conditional statements to determine the appropriate award.

---

## Key Concepts

### 1. **Program Overview**
The program asks the user to input the time taken (in minutes) for each of the three events in a triathlon:
- Swimming
- Cycling
- Running

It then calculates the total time and awards the participant based on the following criteria:
- **Honorary Colours**: Total time is less than 100 minutes.
- **Honorary Half Colours**: Total time is between 100 and 105 minutes.
- **Honorary Scroll**: Total time is between 106 and 110 minutes.
- **No Award**: Total time is more than 110 minutes.

---

### 2. **Steps to Build the Program**

#### Step 1: Collect User Input
Use the `input()` function to collect the time taken for each event. Convert the input to integers for calculations.

```python
swimming_time = int(input("Enter the swimming time (in minutes): "))
cycling_time = int(input("Enter the cycling time (in minutes): "))
running_time = int(input("Enter the running time (in minutes): "))
```

#### Step 2: Calculate Total Time
Add the times for all three events to get the total time.

```python
total_time = swimming_time + cycling_time + running_time
print(f"Total time: {total_time} minutes")
```

#### Step 3: Determine the Award
Use conditional statements (`if`, `elif`, `else`) to determine the award based on the total time.

```python
if total_time < 100:
    print("Within the qualifying time: Honorary Colours")
elif total_time <= 105:
    print("Within five minutes of the qualifying time: Honorary Half Colours")
elif total_time <= 110:
    print("Within 10 minutes of the qualifying time: Honorary Scroll")
else:
    print("More than 10 minutes off from the qualifying time: No Award")
```

---

### 3. **Complete Program**

```python
# Triathlon Award Program

# Step 1: Collect User Input
swimming_time = int(input("Enter the swimming time (in minutes): "))
cycling_time = int(input("Enter the cycling time (in minutes): "))
running_time = int(input("Enter the running time (in minutes): "))

# Step 2: Calculate Total Time
total_time = swimming_time + cycling_time + running_time
print(f"Total time: {total_time} minutes")

# Step 3: Determine the Award
if total_time < 100:
    print("Within the qualifying time: Honorary Colours")
elif total_time <= 105:
    print("Within five minutes of the qualifying time: Honorary Half Colours")
elif total_time <= 110:
    print("Within 10 minutes of the qualifying time: Honorary Scroll")
else:
    print("More than 10 minutes off from the qualifying time: No Award")
```

---

### 4. **Example Output**

#### Example 1:
```
Enter the swimming time (in minutes): 30
Enter the cycling time (in minutes): 40
Enter the running time (in minutes): 25
Total time: 95 minutes
Within the qualifying time: Honorary Colours
```

#### Example 2:
```
Enter the swimming time (in minutes): 35
Enter the cycling time (in minutes): 45
Enter the running time (in minutes): 30
Total time: 110 minutes
Within 10 minutes of the qualifying time: Honorary Scroll
```

#### Example 3:
```
Enter the swimming time (in minutes): 40
Enter the cycling time (in minutes): 50
Enter the running time (in minutes): 35
Total time: 125 minutes
More than 10 minutes off from the qualifying time: No Award
```

---

## Additional Concepts

### 1. **Data Types in Python**
Python supports various numeric data types, including:
- **Integers**: Whole numbers, positive or negative.
  ```python
  class_list = 25  # Integer
  ```
- **Floats**: Decimal numbers or numbers with a fractional component.
  ```python
  interest_rate = 12.23  # Float
  ```
- **Complex Numbers**: Numbers with a real and imaginary part.
  ```python
  c = complex(4, 5)  # 4 + 5j
  ```

### 2. **Casting Between Numeric Data Types**
You can convert between data types using functions like `int()`, `float()`, and `complex()`.
```python
num1 = 12
num2 = 99.99
print(int(num2))  # Output: 99 (data loss occurs)
```

### 3. **Arithmetic Operations**
Python supports basic arithmetic operations like addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), modulus (`%`), and exponentiation (`**`).
```python
total = 2 + 4
print(total)  # Output: 6
```

### 4. **Mathematical Functions**
Python provides a variety of built-in mathematical functions through the `math` module.
```python
import math
print(math.sqrt(16))  # Output: 4.0
print(math.ceil(3.2))  # Output: 4
print(math.floor(3.7))  # Output: 3
```

### 5. **Conditional Statements**
Conditional statements allow you to control the flow of your program based on certain conditions.
```python
num = 10
if num < 12:
    print("The variable num is lower than 12")
elif num > 13:
    print("The variable num is higher than 13")
else:
    print("The variable num is 13")
```

### 6. **Logical Operators**
Logical operators are used to combine multiple conditions.
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

## Conclusion
The Triathlon Award Program demonstrates how to use user input, arithmetic operations, and conditional statements to create a dynamic and interactive Python program. It’s a great example of how Python can be used to solve real-world problems.

---

### Additional Resources
- [Python Documentation: Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python: Conditional Statements](https://realpython.com/python-conditional-statements/)

---
