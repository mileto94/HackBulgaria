import unittest
import create_db
import sqlite3
import glob
import os


class TestMovie(unittest.TestCase):
    """docstring for TestMovie"""

    def setUp(self):
        create_db.create_database("test_catalog.db")
        self.connectionT = sqlite3.connect("test_catalog.db")
        self.pointer = self.connectionT.cursor()
        self.data_movies = create_db.get_movies_data()
        self.data_actors = create_db.get_actors_data()

    def test_create_database(self):
        databases = glob.glob("*.db")
        self.assertIn("movie_catalog.db", databases)

    def test_insert_movie(self):
        for movie in self.data_movies:
            create_db.insert_movie(movie, self.pointer)
        expected = self.pointer.execute("SELECT movie_id, title FROM movies WHERE rating = ?", (10,)).fetchall()
        data_table = self.pointer.execute("SELECT movie_id, title FROM movies").fetchall()
        for movie in expected:
            self.assertIn(movie, data_table)

    def test_insert_actor(self):
        for actor in self.data_actors:
            create_db.insert_actor(actor, self.pointer)
            self.connectionT.commit()
        expected = self.pointer.execute("SELECT actor_id, name FROM actors WHERE name = ?", ("Jason Statam",)).fetchall()
        data_table = self.pointer.execute("SELECT actor_id, name FROM actors").fetchall()
        for actor in expected:
            self.assertIn(actor, data_table)

    def test_insert_actor_again(self):
        for actor in self.data_actors:
            create_db.insert_actor(actor, self.pointer)
            self.connectionT.commit()
        expected = self.pointer.execute("SELECT actor_id, name FROM actors WHERE name = ?", ("Jason Statam",)).fetchall()
        data_table = self.pointer.execute("SELECT actor_id, name FROM actors").fetchall()
        for actor in expected:
            self.assertIn(actor, data_table)

    def test_add_movie(self):
        create_db.insert_movie({"title": "Twin Dragons", "year": 2007, "rating": 8}, self.pointer)
        expected = self.pointer.execute("SELECT actor_id, name FROM actors WHERE name = ?", ("Jackie Chan",)).fetchone()
        data = self.pointer.execute("SELECT actor_id, name FROM actors").fetchall()
        for actor in expected:
            self.assertIn(expected, data)

    def tearDown(self):
        os.remove("test_catalog.db")

if __name__ == '__main__':
    unittest.main()
