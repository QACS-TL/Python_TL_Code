#! /bin/python
# Name:        demo_random_rw_binary.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to Interact with the
# file system by opening/closing file handles random reading using the
# seek() and tell() file handle methods.
"""
    Read movie data randomly from a binary file.
"""

import sys

def main():
    """ Demonstrate random reading from a BINARY file. """


    filename = r"C:\labs\movies.txt" # Always use a raw string for paths.
    SOF = 0 # Start of file.
    CUR = 1 # Current Position.
    EOF = 2 # End of file.

    # Open file handle for READING in BINARY mode.
    fh_in = open(filename, mode="rb")

    # Seek to char position 50 from SOF and read next 30 bytes.
    fh_in.seek(50, SOF)
    text = fh_in.read(30)
    print(f"Text = {text} at position {fh_in.tell() - len(text)}")

    # Seek forwards 30 chars from current position and read next 40 bytes.
    fh_in.seek(30, CUR)
    text = fh_in.read(40)
    print(f"Text = {text} at position {fh_in.tell() - len(text)}")

    # Seek backwards 40 chars from EOF and read next 20 bytes.
    fh_in.seek(-40, EOF)
    text = fh_in.read(20)
    print(f"Text = {text} at position {fh_in.tell() - len(text)}")

    fh_in.close()  # Flush buffers and close file handle.
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)

