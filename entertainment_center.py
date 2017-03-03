#!/bin/env python2

import fresh_tomatoes
import media

def parse_data(file_name): # read and parse movie list from file
    movies = []
    with open(file_name,"r") as f:
        for line in f:
            trailer_url, title, poster_url = line.strip().split() # separated by whitespace
            title = title.replace("_"," ") # replace '_' with ' ' in movie titles because using ' ' in file confuses str.split()
            movies.append(media.Movie(trailer_url,title, poster_url))

    return movies

if __name__ == "__main__":
    movies = parse_data("movies.txt") # hardcoded file name ¯\_(ツ)_/¯
    fresh_tomatoes.open_movies_page(movies) # dynamically generate html file using list of movies
