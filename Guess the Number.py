# Python's built-in module that you can use to make random numbers.
import random

# Return a number between 1 and 10 (both included)
random_num = random.randint(1, 11)
print(random_num)
# Checking multiple conditions
while True:

    # Taking input from user and storing it a variable
    user_input = int(input('Guess the Number: '))

    # Check user input is less than or greate than specified range
    if user_input > 11 or user_input < 1:
        print('Please Guess the Number in Between 1 and 10')

    # If user input is not equal to random number, print error message
    elif user_input != random_num:
        print('Wrong Guess, Try Again')

    # Else print success message and stop the loop using break
    else:
        print("Congratulations! you Won!!")
        break