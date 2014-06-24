import sqlite3


def create_database(db_name):
    connection = sqlite3.connect(db_name)
    c = connection.cursor()

    create_table(c)
    data_movies = get_movies_data()
    for data_movie in data_movies:
        insert_movie(data_movie, c)
    data_actors = get_actors_data()
    for data_actor in data_actors:
        insert_actor(data_actor, c)

    connection.commit()
    connection.close()


def get_movies_data():

    return [{"title": "The Tuxedo", "year": 2006, "rating": 10},
            {"title": "Homefront", "year": 2013, "rating": 9},
            {"title": "Non Stop", "year": 2014, "rating": 10},
            {"title": "Accidental Spy", "year": 2004, "rating": 10},
            {"title": "Hansel & Gretel: Witch Hunters", "year": 2013, "rating": 5},
            {"title": "Taken", "year": 2008, "rating": 10},
            {"title": "Taken 2", "year": 2010, "rating": 10},
            {"title": "Transporter", "year": 2006, "rating": 10}]


def get_actors_data():
    return ["Jackie Chan", "Jason Statam", "Liam Neeson", "Jeremy Renner", "Gemma Arterton"]


def create_table(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS movies (movie_id INTEGER PRIMARY KEY, title text, year int, rating int)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS actors (actor_id INTEGER PRIMARY KEY, name text)""")


def insert_movie(movie, cursor):
    title = movie["title"]
    year = movie["year"]
    rating = movie["rating"]
    cursor.execute("INSERT INTO movies(title, year, rating) VALUES(?, ?, ?)", (title, year, rating))

# def update_movie(movie, cursor):
#     title = movie["title"]
#     year = movie["year"]
#     rating = movie["rating"]
#     cursor.execute()


def get_movies(c):
    return c.execute("SELECT * FROM movies").fetchall()


def get_actors(c):
    return c.execute("SELECT * FROM actors").fetchall()


def insert_actor(actor, cursor):
    name = actor
    cursor.execute("INSERT INTO actors(name) VALUES(?)", (name,))
