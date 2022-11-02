#! /bin/python
# Name:        demo_nested_function.py
# Author:      QA2.0, Pete Behague
# Revision:    v1.0
# Description: This program will demonstrate how to
# use a nested function
"""

"""
import sys

# Example of a nested function to calculate factorials


def factorial(number):
    # Validate input
    if not isinstance(number, int) or number < 0:
        return "Error: 'number' must be an integer and greater than or equal to zero."
    # Calculate the factorial of number

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

def main():
    print(factorial("BAH"))
    print(factorial(6))
    print(factorial(-1))
    print(factorial(5))


if __name__ == "__main__":
    main()
    sys.exit(0)