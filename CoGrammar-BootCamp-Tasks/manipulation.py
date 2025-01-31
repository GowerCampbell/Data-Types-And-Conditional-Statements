# Data Type & Conditions Task 1 Written by Gower Campbell.

# Objective: To demonstrate my knowledge of string manipulation by working with user input.

# ********* Step 1 **********
# i. Calculate and display the length of str_manip

# Prompt the user to input the entire English alphabet
str_manip = input("\nPlease type out the entire English alphabet: ")

# Ensure the user inputs all 26 characters of the English alphabet
if len(str_manip) == 26:
    print("Great! You typed the full alphabet.")
else:
    print("It looks like you didn't type the full alphabet. Please try again.")
    exit()  # Exit the program if the input is invalid

# Calculating String Length using the len() function
print("I see you wrote this many characters: {}".format(len(str_manip)))

# ********* Step 2 **********
# ii. Find the last character in str_manip sentence.

# Get the last character of the string
last_character = str_manip[-1]
print(f"\nHere we take the last letter of the alphabet: {last_character}")

# Replace every occurrence of this letter/character with a '@'
str_manip_replaced = str_manip.replace(last_character, "@")
print("\nAbrakadabra!!! I replaced every '{}' with an '@'!".format(last_character))
print("Modified string: ", str_manip_replaced)

# ********* Step 3 **********
# iii. Print the last three characters in str_manip backwards.

# Get the last three characters and reverse them
last_three_backwards = str_manip[-1:-4:-1]
print("\nBe amazed!! I can even reverse the last three characters: {}".format(last_three_backwards))

# Output: @yw
# This includes the @ character if the last character was replaced.

# ********* Step 4 **********
# iv. Create a five-letter word that is made up of the first three characters 
# and the last two characters in str_manip.

# Get the first three characters and the last two characters
first_three = str_manip[:3]
last_two = str_manip[-2:]

# Concatenate them to form a five-letter word
five_letter_word = first_three + last_two
print("\nAnd combine them almost together: {}".format(five_letter_word), "Mahahaha!!!")

# Using the "+" operator to CONCATENATE them. Code Well!!
