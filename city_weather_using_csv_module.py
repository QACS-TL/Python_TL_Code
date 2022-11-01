#! /bin/python
# Name:        city_weather_using_csv_module.py
# Author:      QA2.0, Donald Cameron
# Revison:     v1.0
# Description: This program will review the topics covered in
# the QA 2.0 Digital session including objects, string handling,
# file interaction, flow control, simple exception handling
# and importing.
"""
    Display City weather information
"""
import csv

def c_to_f(temp):
    """ Return temp in Fahrenheit """
    return (float(temp) * 9/5) + 32

def mm_to_inch(height):
    """ Return precipitation in inches """
    return float(height)/25.4


# file = input("Enter filename: ")
file = "C:\\labs\\capitals.txt"

try:
    # Open file handle for reading in Text mode.
    with open(file, mode="rt") as csvfile:
        # Print header line.
        print(f"{'City':<15s} {'Pop':>10s} {'Rainfall':>8s} {'Temp':>7s}")
        print("-" * 43)

        rows = csv.reader(csvfile, delimiter=',')
        for line in rows:
            city, pop, temp, rain = line
            temp_f = c_to_f(temp) # Convert into fahrenheit.
            rain_i = mm_to_inch(rain) # Convert into inches.
            print(f"{city.title():<15s} {pop:>10s}"
                  f" {rain_i:>7.3f}\N{double prime}"
                  f" {temp_f:>6.2f}\N{degree fahrenheit}")
            # Automatically close file handle.
    print("-" * 43)
except:
    print(f"Error - could not open file {file}")
