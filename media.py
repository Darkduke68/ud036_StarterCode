"""A package provides Movie class."""

import webbrowser

class Movie(object):
    """A class stores various information of a movie.

    Attributes:
        title: Title of the movie.
        poster_image_url: poster image url of the moive.
        trailer_youtube_url: url of youtube trailer.
    """

    def __init__(self, title, image_url, youtube_url):
        self.title = title
        self.poster_image_url = image_url
        self.trailer_youtube_url = youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)