import random
import string

print("Welcome to the Generator Password in Python!")

def password_generator(Len_pass):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    password = "" 
    for i in range(0, Len_pass):
        digit = random.choice(options)
        password = password + digit

    return password

choice_user = input("How many digits do you want? ")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Error: Invalid Digit")
    quit()

response = password_generator(Len_pass = choice_user)
print(f"The password is: {response}")