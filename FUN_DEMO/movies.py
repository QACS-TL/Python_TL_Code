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
# import imdb
from PyMovieDb import IMDB
import re

movie_menu = """
    Movies Menu
    -----------
    1. Get online movie ranking from IMDB
    2. Display top ranking movies
    3. Search for movie
"""

def get_movies():
    """ Get the top 50 movies online from IMDb """
    ia = IMDB()
    #  ia = imdb.IMDb()
    ranked_movies = {}
    # Returns 50 movies in a single string with lots of newline (\n) characters and header information
    pop_movies = ia.popular_movies(genre=None, start_id=1, sort_by=None)
    # Clean up the data by removing newline chars
    pop_movies = pop_movies.replace("\n", "")
    # Clean up the data by removing header info (by searching for the index of the first square bracket ([)
    index = pop_movies.find("[",1)
    # Slice the data to leave just the movies (the -1 ensures the final closing curly brace is also removed.
    pop_movies = pop_movies[index:-1]
    # pop_movies should be a string that has the structure of a list of dictionaries "[{a:b, c:d,..}{...}{...}]"
    # Python’s eval() allows you to evaluate arbitrary Python expressions from a string-based or
    # compiled-code-based input. This function can be handy when you’re trying to dynamically evaluate Python
    # expressions from any input that comes as a string or a compiled code object.
    # (https://realpython.com/python-eval-function/)
    # So, convert the string to become a list of dictionaries
    movies = list(eval(pop_movies))
    # The database used by the API host appears to be a bit corrupt because amongst the "good" data it returns a lot
    # of repeated rows (e.g. currently (06/02/2024) the film called "Deep Fear" is repeated 18 times at the end of the result
    # set.
    # So, the following block filters out any films with the same id
    films = []
    i = 0
    while i < len(movies):
        if films.count(movies[i]["id"]) == 0:  # see if film is already in list
            films.append(movies[i]["id"])  # Create growing list of id's
        else:
            print(movies[i])  # prints repeated movie's details
            del movies[i]
            i -= 1
        i += 1

    # Generate ranked list of movie names
    for rank, movie in enumerate(movies, start=1):
        ranked_movies[rank] = movie["name"]
        if rank >= 50:
            break

    return ranked_movies

def display_movies(movies, top):
    """ Display top movies in a given dict """
    if not movies:
        print("No movies")
    else:
        for rank, name in movies.items():
            print(f"{rank:>4d}: {name:<30s}")
            if int(rank) == int(top):
                break
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
            maxi = input("How many top movies do you want [default=50]: ")
            if not maxi:
                maxi = 50
            display_movies(films, maxi)
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
