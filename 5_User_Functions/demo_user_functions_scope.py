#! /bin/python
# Name:        demo_user_functions_scope.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate the scope (life + visibility)
# of variables/objects
"""
    Displays greeting local and global messages.
"""
import sys

message = "What...is your favourite colour?"


# Example of a user defined function with parameter passing
# and optional defaults
def say_hello(greeting="welcome", recipient="brave knights"):
    """ Display a given greeting to a recipients """

    global message # Try executing with and without this line commented.

    # An assignment to message forces Python to create a new local object.
    message = str(greeting) + " " + str(recipient)
    print(message)

    # return None
    return None


def main():
    """ Main function - say hello to our friends """

    say_hello()
    # print(f"function return is {say_hello()}")

    print(message)

    return None


if __name__ == "__main__":
    main()
    sys.exit(0)
