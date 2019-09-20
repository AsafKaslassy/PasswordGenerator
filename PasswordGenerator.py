import re
import sys
import string
import random
'''
generates a password with
with no duplicate characters in the password
'''

Easy = string.ascii_letters
Medium = string.ascii_letters + string.punctuation
Hard = string.ascii_letters + string.punctuation + string.digits
numbers = list(range(1, 93))
fail_message = " not a valid option ! try again"
CRED = '\033[91m'
CEND = '\033[1m'

# password_complexity = [Easy,Medium,Hard]



def password_generator():
    """
    :return:
    """
    var = 1
    while var == 1:
        allowed = ['Easy','Medium','Hard']
        allowed_lower = (list(map(lambda x:x.lower(),allowed)))
        user_char_complexity = input ("Password Complexity (Easy/Medium/Hard) :  ")
        if user_char_complexity in allowed_lower or allowed:
            if user_char_complexity == 'a':
                user_char_complexity = Hard
            else:
                print('\t',CRED+fail_message+CEND,'\n')
                continue
        else:
            print('\t',CRED+fail_message+CEND,'\n')
            continue

        while var == 1:
            try:
                password_length = int(input ("Password Length (1-90):  "))
                if password_length in numbers:
                    password =  "".join(random.sample(user_char_complexity,password_length ))
                    print ("your generated password is : ", password)
                    break
            except ValueError:
                print(" not a valid option ! try again1")
                continue

            # TODO:
            # check random.random

if __name__ == '__main__':
    password_generator()
    print('PassWord_Generator V1.0 started...')