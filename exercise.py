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

    VOWELS = ["a", "e", "i", "o", "u"]

    if alphabet_letter.isalpha() == False:
        print(f"Invalid input. Please, enter a letter in the alphabet.")

    elif alphabet_letter in VOWELS:
        print(f"The letter {alphabet_letter} is a vowel")
    
    else:
        print(f"The letter {alphabet_letter} is a consonant.")

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

def calculate_dog_years():
    dog_age = input("Input a dog's age in human years: ")

    if dog_age.isalpha() == True:
        print(f"Please, enter a number.")

    elif int(dog_age) <= 2:
        converted_age = int(dog_age) * 10
        print(f"The dog's age in dog years is {str(converted_age)}.")

    else:
        converted_age = 20 + (int(dog_age) - 2) * 7
        print(f"The dog's age in dog years is {str(converted_age)}.")

calculate_dog_years()

#/ ------------------------------- /#
# Exercise 4: Weather Advice

def weather_advice():
    is_it_cold = input('Is it cold? (yes/no). ').lower()
    is_it_raining = input('is it raining? (yes/no). ').lower()
    
    if is_it_cold == "yes" and is_it_raining == "yes":
        print("Wear a waterproof coat.")
    elif is_it_cold == "yes" and is_it_raining == "no":
        print("Wear a warn coat.")
    elif is_it_cold == "no" and is_it_raining == "yes":
        print("Carry an umbrella.")
    elif is_it_cold == "no" and is_it_raining == "no":
        print("Wear light clothing.")

weather_advice()

#/ ------------------------------- /#
# Exercise 5: What's the Season?

def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").lower()
    day = input("Enter the day of the month: ")
    day = int(day)

    if month in ["dec", "jan", "feb"] or (month == "mar" and day <= 19) or (month == "dec" and day >= 21):
        season = "Winter"
    elif month in ["apr", "may"] or (month == "mar" and day >= 20) or (month == "jun" and day <= 20):
        season = "Spring"
    elif month in ["jul", "aug"] or (month == "jun" and day >= 21) or (month == "sep" and day <= 21):
        season = "Summer"
    elif month in ["oct", "nov"] or (month == "sep" and day >= 22) or (month == "dec" and day <= 20):
        season = "Fall"
    else:
        print("Invalid date. Please check your input.")
        return

    print(f"{month} {day} is in {season}.")

determine_season()
