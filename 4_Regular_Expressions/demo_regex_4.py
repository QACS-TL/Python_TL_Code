#! /bin/python
# Name:        demo_regex_4.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to match and substitute string
# data using the re.py module and the sub() and subn() functions. It will also
# introduce Regex flags such as ignore case.
"""
    Search and substitute strings using regular expressions.
"""
import sys
import re

def main():
    """ Executed directly when run as a program """
    # This str object is storing login data for the root user from a
    # a file /etc/passwd on the Linux file system.
    line = "root:x:0:0:The root User:/root:/bin/sh"

    # The sub() function returns the modified string.
    line = re.sub(r"[rR]oot [Uu]ser", r"Administrator", line)
    print(f"Modified line = {line}")

    # The sub() function returns the modified string.
    line = re.sub(r"/bin/sh", r"/bin/bash", line)
    print(f"Modified line = {line}")

    # 4_Regular_Expressions are GREEDY by default and match the largest pattern by default.
    line = "root:x:0:0:The root User:/root:/bin/sh"
    line = re.sub(r"^(root).*\1", r"I am greedy", line)
    print(f"Modified line = {line}")

    # 4_Regular_Expressions - non GREEDY to match the smallest pattern (use additional question mark).
    line = "root:x:0:0:The root User:/root:/bin/sh"
    line = re.sub(r"^(root).+?\1", r"I am not greedy", line)
    print(f"Modified line = {line}")

    # The subn() function returns a TUPLE of (modified string, num changes).
    line = "root:x:0:0:The root User:/root:/bin/sh"
    (line, num) = re.subn(r"[rR]oot", r"Groot", line)
    print(f"Modified line = {line} with {num} changes")

    # Search and replace string with optional RE flags (introduced Py3.1).
    line = "root:x:0:0:The root User:/root:/bin/sh"
    # The optional flags can be set several different ways.
    line = re.sub(r"root user", r"Administrator", line,
                  flags=re.IGNORECASE|re.MULTILINE)
    line = re.sub(r"root user", r"Administrator", line, flags=re.I|re.M)
    # line = re.sub(r"(?im)root user", r"Administrator", line)
    # line = re.sub(r"(?i:r)oot (?i:u)ser", r"Administrator", line) # Python 3.6.
    print(f"Modified line = {line}")

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)