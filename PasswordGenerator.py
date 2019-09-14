import random
import re
import sys
'''
generates a password with
with no duplicate characters in the password
'''

Easy = "abcdefghijklmnopqrstuvwxyz0123456789"
Medium = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Hard = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"

# password_complexity = [Easy,Medium,Hard]


while True:
    allowed = ['Easy','Medium','Hard']
    allowed_lower = (list(map(lambda x:x.lower(),allowed)))

    user_char_complexity = input ("Password Complexity (Easy/Medium/Hard) :  ")
    # if not re.match("^[a-z]*$", user_char_complexity):
    # if not re.match("Easy" or "Medium" or "Hard", user_char_complexity):
    try:
        if user_char_complexity == 'Easy' or 'Easy'.lower():
            user_char_complexity = Easy
        elif user_char_complexity == 'Medium' or 'medium':
            user_char_complexity = Medium
        elif user_char_complexity == 'Hard' or 'hard':
            user_char_complexity = Hard


    except ValueError:
        print(user_char_complexity ," is not a valid option ! try again")

    password_length = input ("Password Length :  ")
    try:
        password_length_num = int(password_length)
    except ValueError:
        print(password_length ," is not a valid password length number! try again")

    password =  "".join(random.sample(user_char_complexity,password_length_num ))
    print ("your generated password is : ", password)

    # TODO:
    # check random.random