#! /bin/python
# Name:        demo_sequential_rw.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to Interact with the file
# system by opening/closing file handles for read, write and appending.
"""
    Write and read movie data to a text file.
"""

import sys

def main():
    """ Demonstrate writing and reading to a text file. """
    movies = { "Donald": ["Braveheart", 'Brave', 'Brigadoon'],
               'Mira': ['Matrix', 'Mad Max', 'Magnolia'],
               'Sarah': ['Seven', 'Scream', 'Saving Private Ryan']
    }
    filename = r"C:\labs\movies.txt"  # Always use a raw string for paths.

    # Open file handle for WRITING in text mode.
    fh_out = open(filename, mode="wt")

    # Iterate through Movie keys and write key: objects to file handle.
    for name in movies.keys():
        print(f"{name}: {movies[name]}", end="\n")
        fh_out.write(f"{name}: {movies[name]}\n") # Remember newline.
    fh_out.close() # Flush buffers and close file handle.

    # Open file handle for READING in text mode.
    with open (filename, mode="rt") as fh_in :

        # text = fh_in.read() # Read ENTIRE file into str object.
        # text = fh_in.read(30)  # Read NEXT 30 chars into str object.
        # text = fh_in.readline()  # Read NEXT line into str object.
        # print(text)

        # lines = fh_in.readlines()  # Read ENTIRE file into list object.
        # print(lines)
        # print(f"1st line = {lines[0]}")

        # Iterate through file handle and read one line at a time.
        # for name in open(filename, mode="wt"):
        for name in fh_in:
            print(name, end="")
        #fh_in.close()  # Flush buffers and close file handle.

        return None


if __name__ == "__main__":
    main()
    sys.exit(0)