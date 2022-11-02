#! /bin/python
# Name:        demo_dictionaries.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to create, grow and shrink
# dictionaries and use keys and iterator for loops to access objects within.
# Dictionaries are mutable collections that can store multiple objects and
# access using UNIQUE keys.
"""
    Weather Program to store and display average (temp, precipitation and humidity)
    for UK cities in 2020.
"""
import sys
import pprint

def main():
    """ Display weather info for uk cities """

    # Create a dictionary to store annual average weather information
    # (Mean Temp, Precipitation, Humidity) for UK Cities in 2020.
    weather = {'Glasgow': [9, 53.6, 87],
               'London': [12, 49.7, 81],
               'Edinburgh': [9, 37.9, 81],
               'Manchester': [7, 35.8, 86],
               'Thurso': [6,89.6, 85]
    }

    # Add two new key: objects to weather dictionary.
    weather['Southampton'] = [8, 28.4, 93]
    weather['Inverness'] = [6, 23.5, 83]

    # weather.clear() # Empty dictionary.
    # w_info = weather.copy() # Copy dictionary.
    weather.pop('Thurso', False) # Remove Thurso as not a City. The second parameter is a default value to return if there is nothing to pop
    # weather.popitem() # Remove next key:object found.

    print(f"Number of cities recorded = {len(weather)}")
    print(f"Weather info for Glasgow = {weather['Glasgow']}")
    print(f"Average precipitation = {weather['Glasgow'][1]} mm")

    # ITERATE through the key and objects within the dict.
    # keys() returns a VIEW into next key.
    for city in weather.keys():
        print(f"{city} average = {weather[city]}")

    # ITERATE through the key and objects within the dict.
    # keys() returns a VIEW into next key.
    for city in weather:
        print(f"{city} average = {weather[city]}")

    # ITERATE through the values within the dict.
    # values() returns a VIEW into the next value.
    for w_info in weather.values():
        print(f"{w_info}")

    # ITERATE through the (values, objects) within the dict.
    # items() returns a VIEW into the next pair of (key, value).
    for city, w_info in weather.items():
        print(f"{city} weather info = {w_info}")

    return None


if __name__ == "__main__":
    main()
    sys.exit(0)