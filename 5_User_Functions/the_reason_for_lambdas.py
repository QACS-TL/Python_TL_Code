#! /bin/python
# Name:        demo_the_reason_for_lambdas.py
# Author:      QA2.0, Pete Behague
# Revision:    v1.0
# Description: This program will demonstrate how to
# define, name and execute lambdas
"""
    The power of lambda is better shown when you use them as an anonymous function inside another function.

    Say you have a function definition that takes one argument,
    and that argument will be multiplied with an unknown number:
"""
import sys

# Example of a user defined function

#def mydoubler(a):
 #   return a * 2

#def mytripler(a):
#    return a * 3

def myfunc(n):
  return lambda a : a * n


def main():
    """ Main function """
    mydoubler = myfunc(2)
    mytripler = myfunc(3)

    print(mydoubler(11))
    print(mytripler(11))


if __name__ == "__main__":
    main()
    sys.exit(0)