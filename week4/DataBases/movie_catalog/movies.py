from actors import Actor


class Movie():
    """docstring for Movie"""
    def __init__(self, title, year, rating, cast):
        #self.movie_id = movie_id
        self.title = title
        self.year = year
        self.rating = rating
        self.cast = {}


    def cast_actor(self, actor_id, name):
        self.cast[actor_id] = Actor(name)
