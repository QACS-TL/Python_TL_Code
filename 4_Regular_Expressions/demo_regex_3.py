#! /bin/python
# Name:        demo_regex_3.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to match string
# data using Regular Expressions and pre-compiling the pattern once.
"""
    Search a given file using regular expressions and display
    matched lines.
"""
import sys
import re

def main():
    """ Display lines in a given file which match Regex """
    fh_in = open(r"C:\labs\words", mode="rt")

    # Pre-compile the pattern once if it does not change.
    reobj = re.compile(r"^.{19}$")

    # Iterate through file handle
    for line in fh_in:
        # Pre-compiled pattern stored in reobj object.
        m = reobj.match(line) # Return None or RE Match object.
        # m = re.search(r"^.{19}$", line) # Return None or RE Match object.

        if m:
            print(line, end="")

    fh_in.close()
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
