#! /bin/python
# Name:        demo_user_functions_docstrings.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate another example of
# creating functions with DocStrings, parameter passing, return values.
"""
    Calculator program with Add, Divide and Multiply functionality.
"""
import sys

def multiply(x, z):
    """
    Accepts two numeric parameters and returns product.

    :param x (int|float): Integer or float
    :param z (int|float): Integer or float
    :return (int|float): Numeric product of x and z
    """
    return x * z

def add(x, z):
    """
    Accepts two numeric parameters, adds them and returns sum.

    :param x (int|float): Integer or float
    :param z (int|float): Integer or float
    :return (int|float): Numeric of x summed with z
    """
    return x + z

def divide(x, z):
    """
    Accepts two numeric parameters, divides first by the second and returns result.

    :param x: (int|float) Integer or float
    :param z: (int|float) Integer or float
    :return (str): f-string of x divided by z to 3 decimal places.
    """
    return f"{x/z:.3f}"

def main():
    """ Single Line docstrings are ideal if the function is self explanatory """
    print(f"4 * 3 = {multiply(3,5)}")
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 / 3 = {divide(4, 3)}")

    # An example of a docstring for the built-in print function.
    # print(print.__doc__)
    # An example of a docstring for the sys module.
    # print(sys.__doc__)
    # Displaying the docstring for user functions.
    print(multiply.__doc__)

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
