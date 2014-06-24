import calculator
import unittest

class TestCalculator(unittest.TestCase):
 	"""Test calculator for TestCalculator"""
 	def test_add(self):
 		self.assertEqual(5 + 6, calculator.add(5,6))

 	def test_minus(self):
 		self.assertEqual(5 - 6, calculator.minus(5,6))

 	def test_multiply(self):
 		self.assertEqual(5 * 6, calculator.multiply(5,6))

 	def test_float_division(self):
 		self.assertEqual(5 / 6, calculator.float_division(5,6))

 	def test_integer_division(self):
 		self.assertEqual(20 // 4, calculator.integer_division(20,4))

 	def test_modulo(self):
 		self.assertEqual(21 % 4, calculator.modulo(21, 4))

if __name__ == '__main__':
	unittest.main()