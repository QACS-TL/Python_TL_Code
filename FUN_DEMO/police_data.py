#! /bin/python
# Name:        police_data.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will allow the user to retrieve publicly
# available Police Forces, crime and stop and search information for
# specific areas using simple HTTP GET requests.
"""
    Docstring: This program/module will..
"""
import webbrowser
import requests
import sys
import pprint

app_name = "Welcome to PDCA - the Police Data Crime App"
menu = """     
    Police Data
    -----------
    1. List of Police Forces
    2. Crimes by location
    3. Stop and Search by Location
      
"""
base_url = r"https://data.police.uk/api/"

def getPoliceForces():
    """ Display List of Police forces """
    try:
        full_url = base_url + "forces"
        force_data = requests.get(full_url) # HTTP GET url page.

        for force in force_data.json():
            print(f"{force['id']:>30s}: {force['name']:<20s}")
        print()
    except Exception as err:
        print(f"Error, cannot retrieve info: [{err}]", file=sys.stderr)
    return None

def getCrimeByLoc():
    """ Display Police Crime data for a specific lat/long """
    date = input("Enter a date (YYYY-MM): ")
    location = input("Enter a Lat/Long (eg. 51.506/-0.075 [London Bridge]): ")
    if not location:
        lat = "51.506"
        lon = "-0.075"
    else:
        lat, lon = location.split("/")

    try:
        full_url = base_url + "crimes-at-location?lat=" + lat + "&lng=" + lon + "&date=" + date
        crime_data = requests.get(full_url)
        for crime in crime_data.json():
            print(f"{crime['category']}, {crime['location_type']}, "
                  f"{crime['outcome_status']['category'] if crime['outcome_status'] else 'No Investigation' }, "
                  f"{crime['location']['street']['name']}")
        print()
    except Exception as err:
        print(f"Error, {err.args}", file=sys.stderr)
        return None

    return None

def getStopByArea():
    """ Display Police Stop Data for a specific lat/long """
    date = input("Enter a date (YYYY-MM): ")
    location = input("Enter a Lat/Long (eg. 51.506/-0.075 [London Bridge]): ")
    if not location:
        lat = "51.506"
        lon = "-0.075"
    else:
        lat, lon = location.split("/")

    try:
        full_url = base_url + "stops-street?lat=" + lat + "&lng=" + lon + "&date=" + date
        stops_data = requests.get(full_url)
        for crime in stops_data.json():
            print(f"{crime['object_of_search']!s}: "
                  f"{crime['gender']} ({crime['age_range']}), {crime['type']}, "
                  f"{crime['location']['street']['name']}")
        print()
    except Exception as err:
        print(f"Error {err.args}", file=sys.stderr)
        return None
    finally:
        print()

    return None

def police_menu():
    """ Menu for Police Crime Data """
    while True:
        print(app_name)
        print("-" * len(app_name))
        print(menu)

        option = input("Please choose an option (1-3 [qQ]=quit):")
        if option == "1":
            getPoliceForces()
        elif option == "2":
            getCrimeByLoc()
        elif option == "3":
            getStopByArea()
        elif option.lower() == "q":
            break
        else:
            print("Invalid option")

    return None

def main():
    """ This module can be run directly to retrieve police crime data """
    police_menu()
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)