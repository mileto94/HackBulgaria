import unittest
import game
import os


class TestDungeon(unittest.TestCase):
    """docstring for TestDungeon"""

    def setUp(self):
        self.file_to_create = "dungeon"
        self.file_handle = open(self.file_to_create, "w")
        self.file_contents = "S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S"
        self.file_handle.write(self.file_contents)
        self.file_handle.close()

    def test_get_map(self):
        new_map = game.Dungeon(self.file_to_create)
        self.assertEqual(self.file_contents, new_map.get_map())


    def tearDown(self):
        os.remove(self.file_to_create)


if __name__ == '__main__':
    unittest.main()
