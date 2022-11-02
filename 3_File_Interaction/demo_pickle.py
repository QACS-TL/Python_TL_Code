#! /bin/python
# Name:        demo_pickle.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to preserve Python objects
# (data plus structure) to a file using the pickle module.
"""
    Preserve/Pickle ONE Python object to a file.
"""
import sys
import pickle
import pprint

def main():
    """ Preserve and reload a Python object a file """
    # Create a dict to hold our favourite movies.
    movies = { 'Donald': ['Dracula', 'Deliverance', 'Descendants'],
               'Mira': ['Matrix', 'Mad Max', 'Magnolia'],
               'Sarah': ['Seven', 'Scream', 'Saving Private Ryan']
    }

    # Open file handle in binary write mode for pickling.
    fh_out = open(r"C:\labs\movies.p", "wb")

    # Dump the movies dict to the pickle file using a chosen protocol.
    # pickle.dump(movies, fh_out, protocol=0) # ASCII
    # pickle.dump(movies, fh_out, protocol=4) # Binary space efficient.
    pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL) # protocol=3
    # pickle.dump(movies, fh_out, pickle.HIGHEST_PROTOCOL)  # protocol=4
    fh_out.close()

    # Open file handle in binary read mode for pickling.
    fh_in = open(r"C:\labs\movies.p", "rb")

    # Reload pickled dict from file back into memory.
    films = dict[str, list[str]](pickle.load(fh_in))
    fh_in.close()

    # Display and compare the movies and films dict using the
    # Std Py library module pprint (pretty print)
    print(movies)
    print("-" * 60)
    pprint.pprint(movies)
    print("-" * 60)
    pprint.pprint(films)
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)



