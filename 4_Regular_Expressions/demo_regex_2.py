#! /bin/python
# Name:        demo_regex_2.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to match string
# data using Regular Expressions.
"""
    Search a given file using regular expressions and display
    matched lines and groupings.
"""
import sys
import re

def main():
    """ Demonstrate 4_Regular_Expressions groupings """
    fh_in = open(r"C:\labs\words", mode="rt")

    # Iterate through file handle.
    for line in fh_in:
        # Match 5 char palindromes.
        m = re.search(r"^(.)(.).\2\1$", line) # Return None or RE Match object.
        if m:
            # The match object m has several methods with info about the match.
            print(f"Matched {m.group()} at char pos {m.start()} - {m.end()}, "
                  f"with groups {m.groups()}, "
                  f"first group is {m.groups()[0]}, " # Index tuple 0 = 1st
                  f"or {m.group(1)}") # More Pythonic way as 1 = 1st.

    fh_in.close()
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
