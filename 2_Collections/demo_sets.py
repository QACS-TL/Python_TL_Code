#! /bin/python
# Name:        demo_dictionaries.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to create, grow and shrink
# and combine sets using SET operators and methods.
# Sets are mutable collections that store multiple UNIQUE objects (with no keys).
"""
    The joy of SETS!
"""
import sys

def main():
    """ Combining collections of Brave Knights and Lumber Jacks """
    # Create two sets, one with objects and one empty.
    brave_knights = {'donald', 'brian', 'terry', 'eric', 'michael'}
    lumber_jacks = set() # Creates an empty set.
    # lumber_jacks = {} # Won't work, defaults to dictionary
    my_list = []
    my_other_list = list("stuff", )

    # Sets are Mutable so can be grown (add) and shrunk(pop/remove).
    brave_knights.add('john')
    brave_knights.add('terry') # Sets automatically remove duplicates!
    lumber_jacks.add('donald')
    lumber_jacks.add('michael')
    lumber_jacks.add('graham')

    # brave_knights.pop() # Remove next object found.
    # brave_knights.remove('john') # Remove object by name.

    # Sets can be combined using operators or methods. Remember Venn diagrams?
    # Combine SETS using SET methods.
    print(f"Brave Knights and Lumber Jacks = {brave_knights.union(lumber_jacks)}")
    print(f"Brave Lumber Knights  = {brave_knights.intersection(lumber_jacks)}")
    print(f"Strictly Brave Knights ONLY = {brave_knights.difference(lumber_jacks)}")
    print(f"Everyone BUT Brave Lumber Knights = {brave_knights.symmetric_difference(lumber_jacks)}")
    print("-" * 60)
    # Combine SETS using SET operators.
    my_csv = "banana | apple | orange"
    print(f"Brave Knights and Lumber Jacks = {brave_knights | lumber_jacks}")
    print(f"Brave Lumber Knights = {brave_knights & lumber_jacks}")
    print(f"Strictly Brave Knights ONLY = {brave_knights - lumber_jacks}")
    print(f"Everyone BUT Brave Lumber Knights = {brave_knights ^ lumber_jacks}")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)