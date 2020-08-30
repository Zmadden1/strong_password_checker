"""
Program to notify the user if they have a strong
password, or not.
"""
#!/usr/bin/env python3
import re
__author__ = "Zachary Madden"
__version__ = "Fall 2020"

PATTERN = re.compile(r'[AZaz]+[0-9]+')

'''
this function will determine the strength of a password
by these criteria:
1. At least 8 characters long
2. Inclusion of at least One Number
3. " " Upper Case Letter
4. " " Lower Case Letter
'''
def main():
    is_strong = False
    while not is_strong:
        print("please enter a password for testing")
        user_password = input(": ")
        if len(user_password) < 8:
            print("password must be at least 8 characters long \n")
            continue
        if PATTERN.search(user_password):
            print("Mighty Strong!")
            is_strong = True
        else:
            print("Let's try that again... \n")

if __name__ == "__main__":
    main()
