import unittest
from unittest import mock
from store import coupon_calculations


class MyTestCase(unittest.TestCase):
    def test_under_10(test_price_under_ten):
        with mock.patch('builtins.input', side_effects=[10, 5, .10]):
            assert coupon_calculations.calculate_order() == 10.72


if __name__ == '__main__':
    unittest.main()
