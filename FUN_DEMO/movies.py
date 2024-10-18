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
import requests
from bs4 import BeautifulSoup
import re

MENU_MOVIES = """
    Movies Menu
    -----------
    1. Get online movie ranking from IMDB
    2. Display top ranking movies
    3. Search for movie
    Q. Quit
"""

def get_movies():
    """ Web Scrape the top 250 movies online from letterboxd.com """
    # Base URL of the Letterboxd Top 250 movies page
    base_url = "https://letterboxd.com/jack/list/official-top-250-films-with-the-most-fans/page/{}/"
    top_movies = {} # Movie info - 'title': [rank, rating, img_url]

    # Scrape the first 3 pages (adjust if necessary)
    for page_num in range(1, 4):  # Adjust range according to the number of pages
        url = base_url.format(page_num) # Send a GET request to fetch the page content
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all movie containers
        movie_tags = soup.find_all("li", class_="poster-container")

        # Extract movie details
        for rank, movie in enumerate(movie_tags, start=1 + len(top_movies)):
            title = movie.find('img', class_='image').get('alt')
            link = movie.find('div', class_='really-lazy-load').get('data-target-link')
            rating = movie.get('data-owner-rating')
            full_link = f"https://letterboxd.com{link}"

            top_movies[title] = [rank, rating, full_link]
    return top_movies

def display_movies(movies, top):
    """ Display top movies in a given dict """
    if not movies:
        print("No movies")
    else:
        for movie, info in movies.items():
            rank, rating, link = info
            print(f"{rank:>4d} {movie:<s}, {rating}/10 - {link}")
            if int(rank) == int(top): break
    return None


def search_movies(pattern=r".", movies=None):
    """ Search for pattern in a given dict of movies """
    if not movies:
        print("No movies to search.")
    else:
        movies_matched = 0
        for movie, info in movies.items():
            rank, rating, link = info
            if re.search(pattern, movie, re.IGNORECASE):
                print(f"{rank:>4} {movie:<s}, {rating}/10 - {link}")
                movies_matched += 1
        print(f"{movies_matched} movies matched")
    return None

def menu():
    """ Movie Menu """
    films = {}
    while True:
        print(MENU_MOVIES)
        option = input("Enter option (1-3, [q=quit]): ").strip().lower()

        if option == "1":
            films = get_movies()
            print(f"Fetched {len(films)} movies")
        elif option == "2":
            top = input("How many top movies do you want to display [default=250]: ").strip() or "250"
            display_movies(films, top)
        elif option == "3":
            pattern = input("Enter title search pattern: ").rstrip()
            search_movies(pattern, films)
        elif option == "q":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again")

    return None


def main():
    menu()
    return None


if __name__ == "__main__":
    main()
    sys.exit(0)
