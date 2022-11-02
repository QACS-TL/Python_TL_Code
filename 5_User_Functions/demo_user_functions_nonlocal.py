#! /bin/python
# Name:        demo_user_functions_nonlocal.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate that Python supports nested
# functions global, local and not-so local variables.
"""
    Nested functions and scope.
"""
import sys

knight = "King Arthur"

def who_goes_next():
    """ Who is next to walk the bridge of death? """
    knight = "Sir Robin" # Really?
    def brave_knights():
        nonlocal knight
        knight = "Sir Lancelot" # Of course, Lancelot is far braver!
        return None
    brave_knights()
    print(f"{knight} will go next")
    return None

def main():
    """ Who goes there? """
    who_goes_next()
    print(f"{knight} will go next")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)

