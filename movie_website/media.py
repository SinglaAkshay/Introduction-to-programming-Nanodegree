# -*- coding: utf-8 -*-

#importing webbrowser module into this file
import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self,movie_title,movie_storyline,movie_poster,movie_trailer,launch_date,duration,worldwide_collection):
        # initialize instance of class Movie
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=movie_poster
        self.trailer_youtube_url=movie_trailer
        self.launch_date=launch_date
        self.duration=duration
        self.worldwide_collection=worldwide_collection

    def show_trailer(movie_trailer):
    	#Shows trailer of Movie
    	webbrowser.open(movie_trailer)
