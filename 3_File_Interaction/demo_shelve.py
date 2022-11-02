#! /bin/python
# Name:        demo_shelve.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to preserve  MULTIPLE
# Python objects to a file using the shelve module.
"""
    Preserve/Pickle ONE Python object to a file.
"""
import sys
import shelve
import pprint

def main():
    """ Preserve and reload multiple Python objects a file """
    # Create dictionaries to hold our favourite movies, tv series and music bands.
    movies = { 'Donald': ['Dracula', 'Deliverance', 'Descendants'],
               'Mira': ['Matrix', 'Mad Max', 'Magnolia'],
               'Sarah': ['Seven', 'Scream', 'Saving Private Ryan']
    }

    tv = {'Donald': ["Dad's Army", "Dragon's Den", 'Dallas'],
          'Mira': ['MASH', 'Masterchef', 'Mythbusters'],
          'Sarah': ['Scrubs', 'Sesame Street', 'Star Trek']

    }

    music = {'Donald': ['David Bowie', 'Deacon Blue', 'Duran Duran'],
             'Mira': ['Metallica', 'Madness', 'Meatloaf'],
             'Sarah': ['S Club 7', 'Spandau Ballet', 'Spice Girls']
    }


    # Open file handle in preserving multiple objects.
    db = shelve.open(r"C:\labs\movies")

    # Write key: objects to shelve database.
    db['movies'] = movies
    db['tv'] = tv
    db['music'] = music

    db.close()

    # Open the Shelve file handle again.
    db = shelve.open(r"C:\labs\movies")

    while True:
        # Iterate through db and display itemised keys.
        for key in db:
            print(key)

        # Prompt user to choose key.
        db_key = input("Choose a key to display or q|Q=quit: ")
        if db_key.lower() == "q": break
        pprint.pprint(db[db_key])

    db.close()
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)




