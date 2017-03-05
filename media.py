

class Movie(object):
    """Movie class that stores relevant information for representing a movie on a webpage.

    Attributes:
        trailer_youtube_url (str): youtube URL of movie trailer
        title (str): title of movie
        poster_image_url (str): URL of movie poster
    """

    def __init__(self, trailer_url, title, poster_url):
        self.trailer_youtube_url = trailer_url
        self.title = title
        self.poster_image_url = poster_url
