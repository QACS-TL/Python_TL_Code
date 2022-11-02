#! /bin/python
# Name:        demo_tuples.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to create and access a tuple
# which is an Immutable (Read-only) Ordered Collection of objects.
"""
    Creating, indexing and accessing objects within a Tuple.
"""
import sys

def main():
    """   """
    """
    Tuples are used to store multiple items in a single variable
    A tuple is a collection which is ordered and unchangeable.
    Can spot a tuple because of the round brackets
    """
    scottish_bands = ("The Proclaimers", "Franz Ferdinand", "Primal Scream"
                      , "Simple Minds", "Primal Scream")

    print(f"Scottish bands is of {type(scottish_bands)}")
    print(f"There are {len(scottish_bands)} bands in {scottish_bands}.")

    # We can Index[] and Slice [start:end] a tuple.
    print(f"The 1st band is {scottish_bands[0]}")
    print(f"The last band is {scottish_bands[-1]}")
    print(f"First three bands = {scottish_bands[0:3]}")

    try:
        # But cannot modify a Tuple as it is immutable.
        # Try this without the try/except block.
        scottish_bands[2] = "Deacon Blue"
    except TypeError:
        print("Cannot modify a Tuple")



    print(f"Primal Scream exists {scottish_bands.count('Primal Scream')} ")
          #f"at index {scottish_bands.index('Primal Scream')}")
    return None


if __name__ == "__main__":
    main()
    sys.exit(0)