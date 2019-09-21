'''
__author__ = "Asaf Kaslassy"
__copyright__ = "Copyright 2019"
__license__ = "GPL"
__version__ = "V_0.0.1+pep_8"
__maintainer__ = "Asaf Kaslassy"
__email__ = "Asaf.kaslassy@gmail.com"
__status__ = "Tests"

'''

import os
import sys
import json
import string
import random
import time
import tkinter as tk
from tkinter import simpledialog
'''
generates a password with
with no duplicate characters in the password
'''

complexity = \
    {
    'Easy' : string.ascii_letters,
    'Medium': string.ascii_letters + string.punctuation,
    'Hard' : string.ascii_letters + string.punctuation + string.digits,
    'numbers' : list(range(1, 93))
     }


fail_message = " \t not a valid option ! try again \n"
CRED = '\033[91m'
CEND = '\033[1m'


'''
# window = tk.Tk()
# window.withdraw()
#
# user_input = simpledialog.askstring(title="Password Generator",
#                                     prompt="Password Complexity :  ",
#                                     initialvalue="Easy / Medium / Hard")
#
# while user_input == "" or not user_input:
#     print("ERROR! - Cannot continue without a user input.")
#     window = tk.Tk()
#     window.withdraw()
#     user_input = simpledialog.askstring(title="Password Generator",
#                                         prompt="Password Complexity",
#                                         initialvalue="ERROR! - Cannot continue without a user input,choose complexity")
#
'''


def password_generator():
    """
    :return:
    """
    var = 1
    while var == 1:

        allowed = ['Easy','Medium','Hard']
        allowed_lower = (list(map(lambda x:x.lower(),allowed)))
        time.sleep(0.5)
        user_char_complexity = input (CRED+"Password Complexity (Easy/Medium/Hard) :  "+CEND)
        user_char_complexity = user_char_complexity.lower()
        if user_char_complexity in allowed_lower or allowed:
            if user_char_complexity == 'easy' :
                user_char_complexity = complexity.get('Easy')
                difficulty = allowed[0]

            elif user_char_complexity == 'medium' :
                user_char_complexity = complexity.get('Medium')
                difficulty = allowed[1]

            elif user_char_complexity == 'hard' :
                user_char_complexity = complexity.get('Hard')
                difficulty = allowed[2]

            elif user_char_complexity == 'exit' :
                print ('you chose to exit')
                sys.exit()

            else:
                print(CRED + fail_message + CEND)
                continue
        else:
            print(CRED + fail_message + CEND)

            continue

        while var == 1:
            try:
                password_length = int(input ("Password Length (1-90):  "))
                if password_length in complexity.get('numbers'):
                    password =  "".join(random.sample(user_char_complexity,password_length ))
                    password_output = 'your generated password is : {} \n'.format(password)
                    print (password_output)
                    if not os.path.exists('directory'):
                        os.makedirs('directory')
                    with open('generated_password.txt', 'a') as outfile:
                        outfile.writelines('difficulty: '+ difficulty + ', ')
                        json.dump(password_output , outfile)
                        outfile.write('\n')

                    break
            except ValueError:
                print(CRED + fail_message + CEND)
                continue

            # TODO:
            # check random.random
            # TODO:
            # add working GUI
            # TODO:
            # add option to rememberable passwords
            # TODO:
            # compile with CX_FREEZE

if __name__ == '__main__':
    print('\nPassWord_Generator V1.0 started...\n')
    time.sleep(1)
    password_generator()
