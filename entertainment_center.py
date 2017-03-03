#!/bin/env python2

def parse_data(file_name):
    import media
    movies = []
    with open(file_name,"r") as f:
        for line in f:
            trailer_url, title, poster_url = line.strip().split()
            title = title.replace("_"," ")
            movies.append(media.Movie(trailer_url,title, poster_url))

    return movies

def generate_website(movies):
    import fresh_tomatoes
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    movies = parse_data("movies.txt")
    generate_website(movies)
