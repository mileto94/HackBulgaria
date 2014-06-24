import string_utils
import unittest


class TestStringUtilsForProblem1(unittest.TestCase):
	"""test cases for problem 1 for TestStringUtils"""
	def test_lines(self):
		self.assertEqual(["jcdjcf"] , string_utils.lines("jcdjcf"))
		self.assertEqual(['1','2'], string_utils.lines("1\n2"))

	def test_unlines(self):
		self.assertEqual('a\nb\nc\nd', string_utils.unlines(['a','b','c','d']))

	def test_words(self):
		self.assertEqual(['say', 'hello'], string_utils.words('say hello'))

	def test_unwords(self):
		self.assertEqual("say hello", string_utils.unwords(['say', 'hello']))

class TestSpacify(unittest.TestCase):
	"""test cases for spacify """
	def test_tabs_to_spaces(self):
		self.assertEqual('    string', spacify.tabs_to_spaces('\tstring'))
		self.assertEqual('        hello', spacify.tabs_to_spaces('\t\thello'))
		

if __name__ == '__main__':
	unittest.main()