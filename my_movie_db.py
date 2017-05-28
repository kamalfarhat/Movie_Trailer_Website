import fresh_tomatoes
import media

# Create an instance of class movie for Fury
fury = media.Movie("Fury", "Story of WWII tank crew", "images/fury.jpg",
                   "https://www.youtube.com/watch?v=-OGvZoIrXpg")

# Create an instance of class movie for Pulp Fiction
pulp_fiction = media.Movie("Pulp Fiction", "Two hitmen with a penchant "
                           "for philosophical discussions", "images/pf.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

# Create an instance of class movie for The Godfather
the_god_father = media.Movie("The God Father", "Story of Italian-American "
                             "crime family of Don Carleano!", "images/gf.jpg",
                             "https://www.youtube.com/watch?v=fB_8VCwXydM")

# Create an instance of class movie for The Devil's Advocate
devils_advocate = media.Movie("Devil's Advocate", "Movie about devil games in "
                              "life and how he controls people", "images/da.jpg",
                              "https://www.youtube.com/watch?v=qD6LZwo3kVI")

# Create an instance of class movie for The Green Mile
the_green_mile = media.Movie("The Green Mile", "Lives of Death Row guards are "
                             "affected by one of their charges", "images/gm.jpg",
                             "https://www.youtube.com/watch?v=uDybmxbKf4Y")

# Create an instance of class movie for Martix
matrix = media.Movie("Matrix", "What is life? and What is illusion?!",
                     "images/mx.jpg", "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# Create an array of all movies
movie_list = [fury, pulp_fiction, the_god_father, devils_advocate, matrix,
              the_green_mile]

# Use fresh_tomatoes' open_movies_page function to create the movies web page
fresh_tomatoes.open_movies_page(movie_list)
