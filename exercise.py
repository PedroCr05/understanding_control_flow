#/ ------------------------------- /#
# Exercise 0:
def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

print_greeting()

#/ ------------------------------- /#
# Exercise 1: Vowel or Consonant

def check_letter():
    
    alphabet_letter = input('Enter a single letter "a-z" or "A-Z": ').lower()

    if alphabet_letter.isalpha() == False:
        print(f"Invalid input. Please, enter a letter in the alphabet.")
        return

    VOWELS = ["a", "e", "i", "o", "u"]

    if alphabet_letter in VOWELS:
        print(f"The letter {alphabet_letter} is a vowel")
    
    else:
        print(f"The letter {alphabet_letter} is a consonant.")

# I though of using data typing but that doesn't make any sense.
# I learned about isalpha()
check_letter()

#/ ------------------------------- /#
# Exercise 2: Old enough to vote?

def check_voting_eligibility():
    REQUIRED_AGE = 18

    voter_age = input('Please enter your age: ')
    print (f"You've just typed {voter_age}")

    if voter_age.isalpha() == True:
        print(f"Please, enter a number.")
    else:     
        if int(voter_age) > 0:
            if int(voter_age) > REQUIRED_AGE:
                print(f"You are old enough to vote!")
            else:
                print(f"You must be 18 or older in order to vote.")
        else:
            print(f"This is a negative input. Please type your age.")

# This works but I'm not sure how to go by shrinking this code down. Personally I would not want to use this many conditionals
# Would want to be given another view of solving this.

check_voting_eligibility()
#/ ------------------------------- /#
# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    DOG_YEARS = 7
    PUPPY_YEARS = 2

    dog_age = input("Input a dog's age in human years: ")

    if dog_age.isalpha() == True:
        print(f"Please, enter a number.")
    else:
        if dog_age > PUPPY_YEARS:
            converted_age = int(dog_age) * DOG_YEARS
            print(f"The dog's age in dog years is {str(converted_age)}.")

calculate_dog_years()
