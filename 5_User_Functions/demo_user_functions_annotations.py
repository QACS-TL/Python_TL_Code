#! /bin/python
# Name:        demo_user_functions_annotations.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to
# define, name, call and pass parameters in and return objects back.
"""
    Displays greeting messages.
"""
import sys

# Example of a user function ANNOTATIONS (Py3.5, not enforced)
def say_hello(greeting:str, recipient:str)->str:
    """ Display a given greeting to a recipients """

    # Annotations not enforced by Python so convert parameters
    # into strings for safety.
    message = greeting + " " + str(recipient)
    print(message)

    # return None
    return message


def main():
    """ Main function - say hello to our friends """

    say_hello("Hello", "world")  # Positional parameter passing.
    say_hello(greeting="Salutare", recipient="prieteni")  # Named parameter passing.
    say_hello("Namaste", recipient="mere dost")  # Mixed parameter passing.
    say_hello(recipient="mes amis", greeting="Bonjour")  # Mixed in different order.
    # say_hello(45, 42) # Try passing in an Integer!
    # say_hello()

    # If the function returns an object we can then have the CALLER as
    # a r-value. That means on the RHS of an assignment or embedded within
    # a larger expression.
    # num = say_hello()
    print(f"Default message is {say_hello('Hello', 'world')}")

    # Attributes of functions can be displayed including annotations.
    print(f"Annotations for say_hello() = {say_hello.__annotations__}")

    return None


if __name__ == "__main__":
    main()
    sys.exit(0)

