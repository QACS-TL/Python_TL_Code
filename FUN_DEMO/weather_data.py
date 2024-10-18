#! /bin/python
# Name:        weather_data.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Prompt user for city/country and then will get the online weather
#              from openweather.com, and the latest police incidents from
#              and either: display info in browser tab, save to DB or save to excel file.
#
# Requires:    This program requires a free API key to access online weather

"""
    Get, display and save weather data for a city.
"""

# Required libraries.
import sys
import re  # Provides regexp support
import webbrowser  # Provides functions for opening and displaying html content to web browsers.
import requests
import weather_db
import datetime

menu = """
    Weather Data
    ------------
    1. Get online weather data for city, country
    2. Display weather data to web browser
    3. Save weather data to local database
    4. Query all rows in local database
    5. Query rows for selected city in local database
    6. Delete row in local database
    7. Delete all rows in local database
    8. Drop local database table
    
"""

# 8-wind compass rose
compass = ["North", "North East", "East", "South East", "South", "South West",
           "West", "North West", "North"]

# API KEY ONLY TO BE USED IN CLASSROOM DEMONSTRATIONS!
# PLEASE subscribe at https://openweathermap.org/api for your own API-KEY.
# API_KEY = os.environ.get("OPEN_WEATHER_API")
API_KEY= "396a2d3386e07f92777ed7fee73f7c67"   # For testing... and to be removed.


def get_weather():
    """ Get weather for a given city, country and return dict """

    city = input("Please enter a city (eg. london): ") or "london"
    country = input("Please enter a country (eg. gb/uk): ") or "gb"

    base_url = r"http://api.openweathermap.org/data/2.5/weather?"
    full_url = f"{base_url}q={city},{country},&appid={API_KEY}"

    try:
        weather_data = requests.get(full_url)
        w_data = weather_data.json()
    except Exception as err:
        # if there was an error opening the url then return error
        print(f"Error: {err.args}", file=sys.stderr)
        return "Error opening url"
    else:
        # if weather_data has message 'city not found' from web server then city is invalid.
        if re.search(r"city not found", weather_data.text):
            print("City Not found", file=sys.stderr)
            return None

    # return the weather condition as a dict.
    return w_data


def display_weather(forecast:'dict')->'None':
    """ Format and display weather information to a browser tab """
    # Parse fields from forecast dictionary.
    city = forecast["name"]
    country = forecast["sys"]["country"]
    desc = forecast["weather"][0]["description"]
    icon = forecast["weather"][0]["icon"]
    icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"
    temp = forecast["main"]["temp"] - 273.15 # Convert Kelvin to Celsius.
    humidity = forecast["main"]["humidity"]
    speed = forecast["wind"]["speed"]
    compass_idx = round(forecast["wind"]["deg"] // 45)
    direction = compass[compass_idx]
    feels_like = forecast["main"]["feels_like"] - 273.15 # Convert Kelvin to Celsius.
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")

    # Format fields into html string plus optional WIDGET
    cel_sign = "\N{degree sign}C"
    outlook = f"""
        <html>
           <head><title>Weather for {city}</title></head> 
           <body<p><a>  Weather for {city}, {country} at {time}</a></p></body>
           <body<p><tr> Weather is {desc} <IMG SRC="{icon_url}" ALT="Weather" WIDTH=64 HEIGHT=64> </tr></p></body>
           <body<p>     Temp is {temp:.0f}{cel_sign} but feels like {feels_like:.0f}{cel_sign} </p></body>
           <body<p>     Wind is {speed} towards {direction}</p></body>
           <body<p>     Humidity is {humidity} </p></body>
           <body></body>
        </html>
    """

    # write forecast to html file
    try:
        with open('weather.html', 'w') as f_html:
            f_html.write(outlook)
    except Exception as err:
        print(f"Error: {err.args}", file=sys.stderr)
        return None

    # display weather forecast to new web browser tab
    try:
        webbrowser.open_new_tab("weather.html")
    except webbrowser.Error as err:
        print(err, file=sys.stderr)
    return None

def weather_menu():
    """ Menu for Weather Data """
    data = weather_db.Weather_db()  # Instantiate DB object
    city_w = {}
    while True:
        print(menu)
        option = input("Enter an option (1-7, [qQ=quit]): ")
        if option == "1":
            city_w = get_weather()
        elif option == "2":
            if city_w:
                display_weather(city_w)
            else:
                print("No weather downloaded")
        elif option == "3":
            data.create_table()
            data.insert_row(table_name="weather", city=f"{city_w['name']}"
                            , country=f"{city_w['sys']['country']}"
                            , wind_direction=f"{city_w['wind']['deg']}"
                            , temp=f"{city_w['main']['temp']}"
                            , date=f"{datetime.datetime.now().date()}")
            data.commit()
        elif option == "4":
            data.query_all()
        elif option == "5":
            data.query_city()
        elif option == "6":
            row = input("Choose a RowID to delete? ")
            data.delete_row(row)
            data.commit()
        elif option == "7":
            data.delete_all_rows()
            data.commit()
        elif option == "8":
            data.drop_table()
        elif option.lower() == "q":
            print("Quitting..")
            break
        else:
            print("Invalid option")

    return None

def main():
    """ This module can be run directly to retrieve weather data """
    weather_menu()
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)