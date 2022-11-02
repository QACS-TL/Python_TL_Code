#! /bin/python
# Name:        demo_user_functions.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to
# define, name and execute (reuse) user defined functions.
"""
    Displays greeting messages.
"""
import sys

# Example of a user defined function
def say_hello():
    """ Display the SAME GREETING to the SAME RECIPIENTS """
    message = "Hello" + " " + "World" 
    print(message)
    return None


def main():
    """ Main function """
    say_hello()  # CALLER - passes control to function say_hello().
    say_hello()  # Can reuse function.
    say_hello()
    say_hello()
    return None


if __name__ == "__main__":
    main()
    sys.exit(0)