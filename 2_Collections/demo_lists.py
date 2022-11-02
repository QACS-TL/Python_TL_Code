#! /bin/python
# Name:        demo_lists.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to create, grow, shrink and access
# objects within a list.
"""
    Playing with a list of numeric (numbers) and non-numeric (movie titles) data.
"""

import sys

def main():
    """ Create, grow, shrink and play with lists (numeric and non-numeric) """
    numbers = [250, 32, 46, 9, 31, 79, 123]
    movies = ['Local Hero', "Gregory's Girl", 'Shallow Grave']

    # A few cool built-in functions for finding, length, smallest
    # largest and sum of numbers.
    print(f"Length of numbers = {len(numbers)}")
    print(f"Smallest number = {min(numbers)}")
    print(f"Largest number = {max(numbers)}")
    print(f"Sum of numbers = {sum(numbers)}")

    # Some of these functions (Not sum) can also be used on non-numeric data.
    print(f"Number of movies = {len(movies)}")
    print(f"1st movie in char order = {min(movies)}")
    print(f"Last movie in char order = {max(movies)}")

    # We can Index and Slice [start:end] lists.
    print(f"1st movie = {movies[0]}")
    print(f"Last movie = {movies[-1]}")
    print(f"Last three movies = {movies[-3:]}")

    # Let's try some list methods for adding to the lhs, rhs
    # and within the list. List will be re-indexed if required.
    movies.append('Trainspotting') # Append one object to RHS.
    movies.extend(['Brave', 'Braveheart']) # Extend multiple objects to RHS.
    movies.insert(0, 'Comfort & Joy') # Insert one object to LHS (before index 0).
    movies.insert(3, "The Angel's Share") # Insert on object before index 3.
    print(f"Scottish movies = {movies}")


    # Let's try some list methods for removing from lhs, rhs
    # and within the list. List will be re-indexed if required.
    last = movies.pop() # Last object removed and optionally returned.
    first = movies.pop(0) # First object removed and optionally returned.
    movies.pop(3) # Remove object at index 3.
    print(f"Scottish movies = {movies}")


    movies.append('Trainspotting') # Append one object to RHS.
    # movies.clear() # Empties List.
    # films = movies.copy() # Copies List.
    # Notice how print parameters can span across lines.
    print(f"I spotted Trainspotting {movies.count('Trainspotting')} "
          f"at index {movies.index('Trainspotting')}")

    # The built-in sorted function returns a sorted list.
    print(f"Movies sorted = {sorted(movies, key=str, reverse=False)}")
    print(f"Movies sorted = {sorted(movies, key=str, reverse=True)}")
    print(f"Movies sorted = {sorted(movies, key=len)}") # Bespoke sort.

    # movies.sort() # Sorts list in place.
    movies.reverse() # Reverses list in place.
    movies.remove('Trainspotting')

    print(f"List of movies = {movies}") # Saturday night viewing.
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)