#! /bin/python
# Name:        demo_collections_comprehensions_plus_c2f.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to filter collections using
# the built-in filter() function, lambda functions and comprehensions.
"""
    Filter collections of cities into warm cities in fahreneit.
"""

import sys

weather = {'Glasgow': 11,
           'London': 21,
           'Edinburgh': 15,
           'Manchester': 18,
           'Thurso': 9
           }

def filter_city(city):
    """ Filter cities by temp """
    if weather[city] >= 15:
        return True
    else:
        return False

def c2f(temp):
    """ Accept temp in celsius and return temp in fahrenheit"""
    return (temp * 9/5) + 32

def main():
    """ Filter collection using filter(), lambda and comprhensions """
    # For Loop plus source collection, optional if condition, and expression.
    warm_cities = {}
    for city in weather: # Iterator for loop + collection.
        if weather[city] >= 15: # Optional condition (filtering)
            warm_cities[city] = c2f(weather[city])  # c2f Expression
    print(f"1.Warm Cities = {warm_cities}")

    # For Loop plus source collection, optional if condition with user function, and expression.
    warm_cities = {}
    for city in weather:
        if filter_city(city):
            warm_cities[city] = c2f(weather[city])
    print(f"2.Warm Cities = {warm_cities}")

    # Built-in filter() function plus source collection, user function for filtering.
    warm_cities = {}
    warm_cities = list(filter(filter_city, weather))
    print(f"3.Warm Cities = {warm_cities}")

    # Built-in filter() function plus source collection, lambda function for filtering.
    warm_cities = {}
    warm_cities = list(filter(lambda city: weather[city] >= 15, weather))
    print(f"4.Warm Cities = {warm_cities}")

    # For Loop plus source collection, optional if condition, and expression. LIST comprehension.
    warm_cities = [ c2f(weather[city]) for city in weather if weather[city] >= 15 ]
    print(f"5.Warm Cities = {warm_cities}")

    # For Loop plus source collection, optional if condition, and expression. TUPLE comprehension.
    warm_cities = [ (city, c2f(weather[city])) for city in weather if weather[city] >= 15 ]
    print(f"5.1.Warm Cities = {warm_cities}")

    # For Loop plus source collection, optional if condition, and expression. DICT comprehension.
    warm_cities = { city: c2f(weather[city]) for city in weather if weather[city] >= 15 }
    print(f"5.2.Warm Cities = {warm_cities}")

    # For Loop plus source collection, optional if condition, and expression. SET comprehension.
    warm_cities = { city for city in weather if weather[city] >= 15 }
    print(f"5.3.Warm Cities = {warm_cities}")

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)