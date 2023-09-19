# Mini Python project that generates a password
# User can choose if he/she wants to include digits or special characters
import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    # container for string characters based on their type
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters  # char container will always have letters
    if numbers:  # if numbers=True
        characters += digits  # add digits to char container
    if special_characters:
        characters += special  # add special to char container

    pwd = ""  # password container
    meets_criteria = False  # based on user input if digits or special is required
    has_number = False
    has_special = False
    # this while loop will generate the random password based on user criteria
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)  # randomly choose character in character container
        pwd += new_char  # place the characters to pwd container

        if new_char in digits:  # if a digit is selected means the password has number
            has_number = True
        elif new_char in special:  # if a special character is selected means the password has special
            has_special = True

        meets_criteria = True
        if numbers:  # if numbers=True then it should have selected digits from new_char
            meets_criteria = has_number
        if special_characters:  # if special_characters=True then it should have selected special from new_char
            meets_criteria = meets_criteria and has_special

    return pwd

# asks the user if he/she wants to generate another password
def new_password():
    while True:
        min_length = int(input("Enter the length of password: "))
        has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
        has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

        pwd = generate_password(min_length, has_number, has_special)
        print("Your password is:", pwd)

        again = input("Do you want to generate another password (y/n)? ").lower()
        if again != "y":
            break


if __name__ == "__main__":
    new_password()
