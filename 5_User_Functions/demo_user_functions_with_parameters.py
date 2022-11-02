#! /bin/python
# Name:        demo_user_functions_with_parameters.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to
# define, name, call and pass parameters in and return objects back.
"""
    Displays greeting messages.
"""
import sys

# Example of a user defined function with parameter passing
# and optional defaults
def say_hello(greeting="ciao", recipient=None):
    """ Display a given greeting to a recipients """

    # Converted parameters to strings for safety!
    # x = greeting + recipient
    # message = str(greeting) + " " + str(recipient)
    message = greeting + " " + recipient
    print(message)
    # return None
    return message


def main():
    """ Main function - say hello to our friends """

    say_hello("Hello", "World")  # Positional parameter passing.
    say_hello(greeting="Salutare", recipient="prieteni")  # Named parameter passing.
    say_hello("Namaste", recipient="mere dost")  # Mixed parameter passing.
    say_hello(recipient="mes amis", greeting="Bonjour")  # Mixed in different order.
    # say_hello("Nazdar", 42) # Try passing in an Integer!
    say_hello()

    # If the function returns an object we can then have the CALLER as
    # a r-value. That means on the RHS of an assignment or embedded within
    # a larger expression.
    # num = say_hello()
    print(f"Default message is {say_hello()}")

    return None


if __name__ == "__main__":
    main()
    sys.exit(0)
