# Asking the user for their age
age = int(input("Enter your age: "))

# Checking if the age is a valid range (between 16 and 100)
if age < 16:
    print("Sorry, you are not old enough to drive.")
elif age > 100:
    print("Hmm, that seems too high. Please enter a valid age.")
else:
    print("You are eligible to drive!")

# Asking the user if they want to check another age
while True:
    user_input = input("Do you want to check another age? (yes/no): ").lower()
    
    if user_input == 'no':
        print("Thanks for using the program. Goodbye!")
        break
    elif user_input == 'yes':
        age = int(input("Enter another age: "))
        if age < 16:
            print("Sorry, you are not old enough to drive.")
        elif age > 100:
            print("Hmm, that seems too high. Please enter a valid age.")
        else:
            print("You are eligible to drive!")
    else:
        print("Invalid input, please type 'yes' or 'no'.")


# Example: A Simple Program
# Let’s create a simple program that performs the following:

# Asks the user for their age.
# Tells the user if they are old enough to drive.
# Checks if their age is valid (between 16 and 100).
# If valid, continues to a loop where the user can keep checking whether they’re eligible to drive until they decide to exit.

# Explanation:
# Variables: We store the user's input in the age variable, which is converted to an integer using int().
# Control Flow:
# The if-elif-else block checks if the age is within the valid range for driving.
# If the age is too low, it tells the user they can't drive. If it’s too high, it asks for a valid age.
# Loops: A while loop continues to ask the user if they want to check another age. The loop will keep running until the user types 'no'.
# Input Validation: We use .lower() to ensure the user’s response is case-insensitive, and handle invalid inputs by prompting the user to try again.
# Try it out:
# You can run this code in any Python environment. When you run it, it will:

# Ask for your age.
# Let you know if you’re eligible to drive or if there’s an invalid input.
# Continue asking if you want to check more ages.