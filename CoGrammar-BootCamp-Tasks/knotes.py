
# DATA TYPES & CONDITIONAL DATA TYPES Written by Gower Campbell

# To guide our codes decisions, behaviour and purpose we use conditiional 
# statements using operators - symbols that tell the compiler or interpetwr 
# what to do in mathematical, relational or logical tasks.

# In Python, strings must be written within quatation marks (" ")
# The smallest possible string contains zero characters and is called 
# an empty string (i.e. string ="") Example:

name = "Linda"

song = "The Bird Song"

license_plate = "CTA 456 GP"

# Medium of communication between the computer and the user.

name = "John"

joke = "Knock, knock, Who's there?"

# Using triple quotes (''' ''') to define multi line string 
# and perserves the formatting of the string. Example:

long_string = '''This is a long string

using triple quotes preserves everything inside it as a string

even on different lines with different \n spacing'''

# Strings can be added to one another through CONCATENATION

name = "Peter"
surname = "Parker"
full_name = name + surname

# full_name stores the value "Peter Parker" The "+" joins the string.

full_name = name + " " + surname

# Note: You cannot Concatenate a string and a non-string..
# You need to cast the non-string to a string.

print(full_name + str(32))

# Formatting strings; .format() method.

name = "Peter Parker"
age = 32

sentence = "My name is {} and I'm {} years old.".format(name, age)

print(sentence)

# Using {} curly braces to serve as placeholders for variables
# The variables will be listed in the orther they fill the placeholder
# of the string...

# However, their is also a shorthand for the format function called 
# F-Strings or just f-strings

name = "Peter Parker"
age = 32

sentence = f"My name is {name} and I'm {age} years old."

print(sentence)

# Writing an f before the string.

# Numbers as strings
# Storing the number in the string.

telephone_num = "041 123 1234"

# Actions That Can Be Performed On Strings

# Indexing: Access individual characters in a string.
# Slicing: Extract a substring from a string
# Extended slicing: Extract a substring with a specfic step.
# Using string method: Utilise built-in methods to manipulate and analyse strings.

#len()
# len() function is a general function that works with various 
# data types, including strings, to return the number of items in 
# an object.

print(len("Hello World!"))

# Output: Counting 12=characters long, including punctuation & spaces

# SLICING or slive
# Extracting characters from a string based on a starting index & ending index.
# Starting position/index 0 and end at position/index 5

greeting = "Hello"

print(greeting[1:4])

# Output: "ell" extracting a "chunk" of characters from a string.

# Negative Numbers
# Starting at the end of the string instead of the beginning.
# Example: The string is printed from the third-to-last character.
# NOTICE that you DON'T need to specify the end of the index range

greeting = "Hello"

print(greeting[-3:])
#Output: llo

#If the starting position is BLANK it will be default 0

greeting = "Hello"
print(greeting[:1])
#Output: H

#Extended Slice
# The syntax is [begin: end : step]
# If the end is left out, the slice contonues to the end of the string.

greeting = "Hello"
print(greeting[1::2])
# Output: "el" From starting from position 1, then continues to the end of the 
# string and skips/steps over every other position to extract 
# the 2 position.

# -1 reverse order argument
# The slice begins from position 4, continues to position 1 
# (not included), and skips/steps backwards one position at a time:

greeting = "Hello"
print(greeting[4:1:-1])

#Output: oll

# You can print a string in reverse by using [::-1]
# Remember for the [begin : end : step ] Specifying a step of -1

new_string = "Hello world"
fizz = new_string[0:5]

print(fizz)
print(new_string)

#Output: 
# Hello
# Hello World!

#Knote: Slicing a string does not modify the orignal string.
# You can caputure a slice from one variable in a separate varable.
# 
#  Using built-in functions I.E. Concatenate strings, search within strings,
# extract sybstrings, and perform various other operations.

# Numbers in Python 
# Integers (Positive or Negative) e.g. num = int("-12") 
# 
# Float: decimal numbers or numbers, which contain a fractional
# component e.g. storing measurements for a building or amounts of money.
# Even Scientific notation, with E or e indicating the power of 10
# E.g x = float("15.20"), y + float("-32.54e100").
# 
#  Complex Numbers: Real & Imaginary part, which are each a 
# floating-point number, eg. c = complex("45.j")

#Declaring Numbers in Python

class_list = 25  #Integer
interest_rate = 12.23  #Float

#Casting Between numeric Data Types
# Converting floats to ints, as below, causes data loss.
# int() removes values after the decimal point only a whole number.

num1 = 12
num2 = 99.99

print(int(num2))

#ARITHMETIC OPERATIONS

total = 2 + 4
print(total)

#Symbols used in Python 
# "+" Addition Adds Values on either side of the operator.
# "-" Substracts the value on the right of the operator from the left
# "*" Multiplication on either side of the operator.
# "/" Division: Divides the values on the left by the right
# "%" Modulus: Divides the value on the left of the operator by the right and returns the remainder.
# E.g. 4 % 2 == 0 but 5 % 2 == 1.


#"**" Exponent: Performs an exponential calculation, i.e. calculates the answer of the value
# on the left to power of the the value on the right.

#Mathematical Functions
# Built-In Function (pre-written code) and libararies importe into my programs.
# e.g. math module offers extensive collection of specialised functions

round()
#Rounds a floating-point number to the nearest whole number, 
# or decimal places as specified by the second argument.
number = 66.6564544
print(round(number,2))

# Will output 66.66

min()
# Returns the smallest value from a iterable, 
# such as a list or tuple.
number_list = [6,4,66,35,1]
print(min(number_list))
#Wiill output 1

max()
# Returns the largest value from an iterable, such as a list or 
# tuple. 
number_list = [6,4,66,35,1]
print(max(number_list))
#Output: 66

sum()
# Calculates the total sum of all elements 
# in iterable such as a list or tuple
number_list = [6,4,66,35,1]
print(sum(number_list))
# Output 112

#Mathematical functions available through the math module/
import math
#Add this to the top of your program

math.floor()
#Rounds anumber down.
print(math.floor(30.33333))
#Output 30

math.ceil() 
#Rounds a number up.
print(math.ceil(30.33333))
#Output: 31.0

math.trunc()
#Cuts off the decimal part of the float.
print(math.trunc(30.3333))
#Output 30

math.sqrt()
#Finds the square root of a number
print(math.sqrt(4))
#Output 2.0

math.pi()
# Returns the value for pi 
# where pi is the number used to calculate the area 
# of a circle.
print(math.pi)
# Output 3.1415

#IF Statement
# Contain a condition following syntax

if condition:
    indented statements

num = 10

if num < 12: # Don't forget the colon!
    print("the variable num is lower than 12")

# < (less than) if it less than 12 it will print

num = int(input("Please input anumber between 1 and 100"))
if num < 12:
    print("The value you entered is lower than 12")
    #Knote you need to cast the input as an int() if we want to 
    # perform operations.
# Notice Syntac Rules for an "if statement"
# A colon ":" is followed by code that runs only if the statement is True
# Indentation or...
# between each line is to show pathway.
# Using brackets, can help with readabiluty when code gets complicated 
# if (num <12):

# Comparison Operators
#To compare values or variables in programming 
#These Operaters work with if statements, if-else statements & loops.

# greater than >
# less than    <
# equal to     ==
# not          !

# Basing your calculations on the result of a boolean vale.
# This value can be changed as the program runs.
pass_word = False
pass_word = True

#Booleans in Control Statements
#Called "Branching" 
# 'if' one condition is 'true', do one thing and 'if the 
# condition is 'false' do something else. 
# Through if-else.... and if-elif-else statements

umbrella = "Leave me at home"
rain = False
if rain:
    umbrella = "bring me with"
    #This is shorthand for "if rain == True" and we only write this if
    # the condition specfically needs to be false.
    # 
    # The structure of IF-ELSE Statements
    # Checking if the condition supplied to the if statement is 'True'
    # It will do something else if false
    # (Start) -> if statement <Condution > 
    # - True [Body of if] - False [body of else] 
    # -> (END)

num = int(input("Plaease input a number between 1 and 100"))
if num < 12:
    print("The value you entered is lower than 12")

else:
    print("The value you entered is higher than 12")

#ELIF Statemenys.
# Stands for "else if".
# Adding more conditions to if statements.
# Testing multiple parameters to the code block.
# Unlike the else statements you can have multiple elif statements.
# in an if-elif-else. Explained:
# 
# If the first elif statement condition is also false, the condition 
# of the next elif statment is chected, etc. After all are false then it 
# the else statemnent and its indented statements is executed.

num = int(input("Plaease input a number between 1 and 100"))
if num < 12:
    print("The value you entered is lower than 12")
elif num > 13:
    print("The value you entered is higher than 13")
elif num < 13:
    print("The value you entered is lower than 13")
else:
    print("The value you entered is 13")

# You cant have an else without an if.

current_time = int(input("Can you tell me the time?"))
if current_time < 11:
    print("Time for a short jpg -lets go!")

elif current_time == 11:
    print("Good Morning")

else:
    print("Its after 11 - its lunch time.")

# The value that the variable hour hold determines, which string 
# is assigned. 

hour = 18
if hour < 18:
    greeting = "Good day"
elif hour < 20:
    greeting = "Good evening"
else: 
    greeting = "Good night"

#Applying Operators; Combining them with "="
# greater tham or equal to.        >=
# less than or equal to            <=
# not equal to                     !=

#Comparing Strings

my_name = "tom"
if my_name == "tom":
    print("hello, tom")

#Comparing Numbers

num1 = 10
num2 = 20

if num1 >= num2:
     print("It's not possible that 10 is bigger than or equal to 20.")
elif num1 <= num2: 
   print("10 is less than or equal to 20.")
elif num1 != num2:
     print('''This is also true since 10 isn't equal to 20, but the elif
statement before comes first and is true, so Python will execute that and
never get to this one!''')
elif num1 == num2:
    print("Will never execute this print statement...")

# Logical Operators
# Used to control flow of a program.
# Found as part of the 'if statement.'
# 
# Allowing the program to make a decision 
# based on multiple condition. 

# Testing more than one 'if statement'

and
#Both conditions need to be TRUE
#for the whole statement to be true.
# (Called the CONJUNCTION OPERRATION)

or 
# At least one condition needs to be TRUE
# for the whole statement to be TRUE.
# (Called the DISJUNCTION OPERATION)

not
# The statement is TRUE if the condition is FALSE
# (Only requires one condition or operands)

#Example of an 'and' operation

team1_score = 3
team2_score = 2
game = "over"

if (team1_score > team2_score) and (game == "Over"):
    print("Congratulations Team 1, you have won the match!")
elif (team1_score < team2_score) and (game == "Over"):
    print("Congratulations Team 2, you have won the match!")

# Example of an 'or' operation

speed = int(input("How many kilometres per hour are you travelling at?"))
belt = input("Are you wearing your saafety belt?")

if (speed > 80) or (belt != "Yes"):
    print("Sorry Sir, but I have to give you a traffic fine.")

# Assignment Operations

=
# Equals: set value of the on the left to that of the right
# e.g. n = 7 

+=
#Plus-equals: Adds 1 to the variable for each iteration
# e.g n += 1 is shorthand for n = n + 1 

-=
#Minus-equals: minuses 1 from the variable for each iteration
# e.g. n -= 1 shortand for n = n - 1
