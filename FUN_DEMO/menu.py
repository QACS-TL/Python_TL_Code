#! /bin/python
# Name:        menu.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Fun demo for QA2.0 Python LIVE
"""
    Docstring: A fun program to allow users to choose from an
    interesting and eclectic list of options including getting the
    latest weather or crime reports from an area, getting the latest
    top 250 movies and interacting with SQLite databases.
    And a little 8_Object_Oriented_Programming for extra fun!
"""
import sys
import police_data
import weather_data
import movies

menu = """
    Fun Data Menu
    -------------
    1. Display Online Public Weather Data to Browser. 
    2. Display Online Public UK Police Data to Screen. 
    3. Display/Search top Movies from IMDb. 

"""

def top_level_menu():
    """ Top Level Menu function for displaying crime, weather and movie data """
    while True:
        print(menu)
        option = input("Enter an option (1-3, [qQ=quit]): ")
        if option == "1":
            weather_data.weather_menu()
        elif option == "2":
            police_data.police_menu()
        elif option == "3":
            movies.menu()
        elif option.lower() == "q":
            print("Quitting..")
            break
        else:
            print("Invalid option")
    return None

def main():
    """ Program can be run directly """
    top_level_menu()
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)