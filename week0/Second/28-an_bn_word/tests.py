import solution
import unittest

class tests_is_an_bn_word(unittest.TestCase):
	
	def tests_self(self):
		self.assertEqual(True, solution.is_an_bn(''))
		self.assertEqual(False, solution.is_an_bn("rado"))
		self.assertEqual(False, solution.is_an_bn("aaabb"))
		self.assertEqual(True, solution.is_an_bn("aaabbb"))
		self.assertEqual(False, solution.is_an_bn("aabbaabb"))
		self.assertEqual(False, solution.is_an_bn("aabbaabb"))
		self.assertEqual(False, solution.is_an_bn("bbbaaa"))
		self.assertEqual(True, solution.is_an_bn("aaaaabbbbb"))


if __name__ == '__main__':
	unittest.main()
