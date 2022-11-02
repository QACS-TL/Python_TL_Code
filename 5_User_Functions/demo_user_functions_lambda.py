#! /bin/python
# Name:        demo_user_functions_lambda.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate another example of
# creating functions using lambda (anonymous) functions.
# Simple one-line docstrings are used.
"""
    Calculator program with Add, Divide and Multiply functionality.
"""

import sys

def multiply(x, z):
    """ Multiply two numeric parameters and return result """
    return x * z

def add(x, z):
    """ Add two numeric parameters and return result """
    return x + z

def divide(x, z):
    """ Divide two numeric parameters and return formatted str """
    return f"{x/z:.3f}"

def main():
    """ This is the main program function """
    print(f"4 * 3 = {multiply(4, 3)}")
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 / 3 = {divide(4, 3)}")

    # A lambda function is a small anonymous function that can take
    # multiple arguments but only has one expression. And is an alternative
    # way to defining simple functions without the 'def' statement.
    l_mul = lambda x, z: x * z
    l_add = lambda x, z: x + z
    l_div = lambda x, z: f"{x/z:.3f}"

    print("-" * 20)

    print(f"4 * 3 = {l_mul(4, 3)}")
    print(f"4 + 3 = {l_add(4, 3)}")
    print(f"4 / 3 = {l_div(4, 3)}")

    print("-" * 20)



    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
