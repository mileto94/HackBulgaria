from order_pizza import OrderPizza
import unittest


class TestOrderPizza(unittest.TestCase):
    """docstring for TestOrderPizza"""
    def setUp(self):
        self.order = OrderPizza([("Alex", 4.56), ("Marty", 5.33), ("Gloria", 6.19)])

    def test_take_order(self):
        expect = [("Alex", 4.56), ("Marty", 5.33), ("Gloria", 6.19), ("Melmon", 9.34)]
        self.order.take_order("Melmon", '2.00')
        self.assertEqual(expect, self.order.take_order("Melmon", 7.34))

    def test_status(self):
        expect = [("Alex", 4.56), ("Marty", 5.33), ("Gloria", 6.19)]
        self.assertEqual(expect, self.order.status_order())

    def test_print_status(self):
        expect = "Alex - 4.56\nMarty - 5.33\nGloria - 6.19"
        self.assertEqual(expect, self.order.print_status())


if __name__ == '__main__':
    unittest.main()
