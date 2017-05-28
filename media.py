import webbrowser


# Define class Movie with 4 variables and 1 method
class Movie:

    # Define the Constructor for class Movie
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        # Variable1: movie title
        self.title = title
        # Variable2: movie story line
        self.storyline = storyline
        # Variable3: movie poster image url
        self.poster_image_url = poster_image
        # Variable4: movie trailer url
        self.trailer_youtube_url = trailer_youtube

    # Method to play movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
