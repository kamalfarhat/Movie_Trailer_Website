This is a program written in Pyhton to dynamically generate a movie trailer website from a data structure, the repository includes a README file, 3 python code files, an images folder that contains 6 images for the movie posters and an HTML output file :

1- media.py 
This is where the class Movie is defined with the following variables and methods:
	- title variable: to store the movie title 
	- story_line variable: to store the movie's story line
	- poster_image variable: to store a link to the movie's poster image 
	- trailer_youtube variable: to store a link to the movie's trailer youtube video
	- show_trailer method: to play the movie trailer youtube video in a new browser 

2- my_movie_db.py (Run this file!)
This is where instances of class movie are created for each of the movies and the fresh tomatoes' is used to create the website

3- fresh_tomatoes.py
This is a code provided by Udacity Instructor that has a function inside it called open_movies_page(), this function takes a list of movies as input and creates an HTML page using the movies' poster images and video trailers as output:

4- fresh_tomatoes.html
This is the movie trailer website which is the final output of the program