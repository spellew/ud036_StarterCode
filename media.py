import webbrowser


class Movie():
    """
    This class provides a way to store movie related information, such as a "
    " movie's title, rating, storyline, poster, and trailer.

    Attributes:
        VALID_RATINGS (list): A movie's possible ratings

    Todo:
        Use an API to retrieve movies and their info, instead of hard coding "
        " it.
    """  # This string can accessed via media.Movie.__doc__

    # This class constant can be accessed by media.Movie.VALID_RATINGS
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # This function is run everytime the class is initiated
    def __init__(
            self,
            movie_title,
            movie_rating,
            movie_storyline,
            poster_image,
            trailer_youtube):
        # The arguments passed to the class contructor, are used to initiate
        # the class object with default values
        self.title = movie_title
        self.rating = movie_rating
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
