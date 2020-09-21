import unittest
from store import coupon_calculations


class MyTestCase(unittest.TestCase):
    def test_under_10(test_price_under_ten):
        test_price_under_ten.assertEqual(10.72, coupon_calculations.calculate_order(10, 5, .10))
        test_price_under_ten.assertEqual(10.46, coupon_calculations.calculate_order(10, 5, .15))
        test_price_under_ten.assertEqual(10.19, coupon_calculations.calculate_order(10, 5, .20))
        test_price_under_ten.assertEqual(9.93, coupon_calculations.calculate_order(10, 5, .25))
        test_price_under_ten.assertEqual(9.66, coupon_calculations.calculate_order(10, 5, .30))
        test_price_under_ten.assertEqual(5.95, coupon_calculations.calculate_order(10, 10, .10))
        test_price_under_ten.assertEqual(5.95, coupon_calculations.calculate_order(10, 10, .15))
        test_price_under_ten.assertEqual(5.95, coupon_calculations.calculate_order(10, 10, .25))
        test_price_under_ten.assertEqual(5.95, coupon_calculations.calculate_order(10, 10, .25))
        test_price_under_ten.assertEqual(5.95, coupon_calculations.calculate_order(10, 10, .30))
    def test_under_30(test_price_under_thirty):
        test_price_under_thirty.assertEqual(10.72, coupon_calculations.calculate_order(20, 5, .10))
        test_price_under_thirty.assertEqual(10.46, coupon_calculations.calculate_order(10, 5, .15))
        test_price_under_thirty.assertEqual(10.19, coupon_calculations.calculate_order(10, 5, .20))
        test_price_under_thirty.assertEqual(9.93, coupon_calculations.calculate_order(10, 5, .25))
        test_price_under_thirty.assertEqual(9.66, coupon_calculations.calculate_order(10, 5, .30))
        test_price_under_thirty.assertEqual(5.95, coupon_calculations.calculate_order(10, 10, .10))
        test_price_under_thirty.assertEqual(5.95, coupon_calculations.calculate_order(10, 10, .15))
        test_price_under_thirty.assertEqual(5.95, coupon_calculations.calculate_order(10, 10, .25))
        test_price_under_thirty.assertEqual(5.95, coupon_calculations.calculate_order(10, 10, .25))
        test_price_under_thirty.assertEqual(5.95, coupon_calculations.calculate_order(10, 10, .30))
if __name__ == '__main__':
    unittest.main()
