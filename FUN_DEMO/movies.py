#! /bin/python
# Name:        movies.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will download the top 250 movies from IMDB
# and will allow the user to display the top-n ranked movies or search for
# for their favourite movies.
"""
    Download and display the Top 250 Movies Data from IMDB.
"""
import sys
import imdb

import re

movie_menu = """
    Movies Menu
    -----------
    1. Get online movie ranking from IMDB
    2. Display top ranking movies
    3. Search for movie
"""

def get_movies():
    """ Get the top 250 movies online from IMDb """
    ia = imdb.IMDb()
    movies = {}

    for rank, movie in enumerate(ia.get_top250_movies(), start=1):
        movies[rank] = str(movie)

    return movies

def display_movies(movies, top):
    """ Display top movies in a given dict """
    if not movies:
        print("No movies")
    else:
        for rank, name in movies.items():
            print(f"{rank:>4d}: {name:<30s}")
            if int(rank) == int(top): break
    return None

def search_movies(pattern=r".", movies=None):
    """ Search for pattern in a given dict of movies """
    if movies is None:
        movies = {}
    if movies:
        for rank, name in movies.items():
            m = re.search(pattern, name, re.IGNORECASE)
            if m:
                print(f"{rank:>4d}: {name:<30s}")
    else:
        print("No movies to search")
    return None

def menu():
    """ Movie Menu """
    films = {}
    while True:
        print(movie_menu)
        option = input("Enter option (1-3, [qQ=quit]): ")
        if option == "1":
            films = get_movies()
        elif option == "2":
            max = input("How many top movies do you want [default=250]: ")
            if not max: max = 250
            display_movies(films, max)
        elif option == "3":
            pattern = input("Enter Regex search pattern: ")
            search_movies(pattern, films)
        elif option.lower() == "q":
            break
        else:
            print("Invalid option")

    return None

def main():
    menu()
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)