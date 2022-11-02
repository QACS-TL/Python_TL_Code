#! /bin/python
# Name:        demo_user_functions_variadic.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to
# define, name, call and pass parameters in and return None.
"""
    Displays greeting messages to ALL friends and foes.
"""
import sys

# Example of a Variadic function.
def say_hello(greeting="ciao", *recipients):
    """
    Accept a greeting string and variable number of recipients and
    display message to ALL recipients and returns None.
    """

    # Use an iterator for loop to iterate through objects in tuple.
    for person in recipients:
        message = str(greeting) + " " + str(person)
        print(message)

    # return None
    return None


def main():
    """ Main function - say hello to our friends """

    # Pass in a variable number of parameters to the function.
    say_hello('None shall pass', 'green knight')
    say_hello('None shall pass', 'green knight', 'arthur', 'patsy')
    say_hello('None shall pass')

    return None


if __name__ == "__main__":
    main()
    sys.exit(0)

