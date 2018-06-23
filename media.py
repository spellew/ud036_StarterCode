import webbrowser;

class Movie():
  """This class provides a way to store movie related information""" # This string can accessed via media.Movie.__doc__
  VALID_RATINGS = ["G", "PG", "PG-13", "R"]; # This class constant can be accessed by media.Movie.VALID_RATINGS
  def __init__(self, movie_title, movie_rating, movie_storyline, poster_image, trailer_youtube): # This function is run everytime the class is initiated
    self.title = movie_title; # The arguments passed to the class contructor, are used to initiate the class object with default values
    self.rating = movie_rating; 
    self.storyline = movie_storyline;
    self.poster_image_url = poster_image;
    self.trailer_youtube_url = trailer_youtube;