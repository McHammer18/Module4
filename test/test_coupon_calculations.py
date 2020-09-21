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
        test_price_under_ten.assertEqual(5.95, coupon_calculations.calculate_order(10, 10, .20))
        test_price_under_ten.assertEqual(5.95, coupon_calculations.calculate_order(10, 10, .25))
        test_price_under_ten.assertEqual(5.95, coupon_calculations.calculate_order(10, 10, .30))
    def test_under_30(test_price_under_thirty):
        test_price_under_thirty.assertEqual(31.80, coupon_calculations.calculate_order(30, 5, .10))
        test_price_under_thirty.assertEqual(30.47, coupon_calculations.calculate_order(30, 5, .15))
        test_price_under_thirty.assertEqual(29.15, coupon_calculations.calculate_order(30, 5, .20))
        test_price_under_thirty.assertEqual(27.82, coupon_calculations.calculate_order(30, 5, .25))
        test_price_under_thirty.assertEqual(26.50, coupon_calculations.calculate_order(30, 5, .30))
        test_price_under_thirty.assertEqual(27.03, coupon_calculations.calculate_order(30, 10, .10))
        test_price_under_thirty.assertEqual(25.97, coupon_calculations.calculate_order(30, 10, .15))
        test_price_under_thirty.assertEqual(24.91, coupon_calculations.calculate_order(30, 10, .20))
        test_price_under_thirty.assertEqual(23.85, coupon_calculations.calculate_order(30, 10, .25))
        test_price_under_thirty.assertEqual(22.79, coupon_calculations.calculate_order(30, 10, .30))
    def test_under_50(test_price_under_fifty):
        test_price_under_fifty.assertEqual(54.88, coupon_calculations.calculate_order(50, 5, .10))
        test_price_under_fifty.assertEqual(52.50, coupon_calculations.calculate_order(50, 5, .15))
        test_price_under_fifty.assertEqual(50.11, coupon_calculations.calculate_order(50, 5, .20))
        test_price_under_fifty.assertEqual(47.72, coupon_calculations.calculate_order(50, 5, .25))
        test_price_under_fifty.assertEqual(45.34, coupon_calculations.calculate_order(50, 5, .30))
        test_price_under_fifty.assertEqual(50.11, coupon_calculations.calculate_order(50, 10, .10))
        test_price_under_fifty.assertEqual(47.99, coupon_calculations.calculate_order(50, 10, .15))
        test_price_under_fifty.assertEqual(45.87, coupon_calculations.calculate_order(50, 10, .20))
        test_price_under_fifty.assertEqual(43.75, coupon_calculations.calculate_order(50, 10, .25))
        test_price_under_fifty.assertEqual(37.63, coupon_calculations.calculate_order(50, 10, .30))

    def test_over_50(test_price_over_fifty):
        test_price_over_fifty.assertEqual(64.42, coupon_calculations.calculate_order(60, 5, .10))
        test_price_over_fifty.assertEqual(54.06, coupon_calculations.calculate_order(65, 5, .15))
        test_price_over_fifty.assertEqual(55.12, coupon_calculations.calculate_order(70, 5, .20))
        test_price_over_fifty.assertEqual(59.62, coupon_calculations.calculate_order(80, 5, .25))
        test_price_over_fifty.assertEqual(59.36, coupon_calculations.calculate_order(85, 5, .30))
        test_price_over_fifty.assertEqual(59.65, coupon_calculations.calculate_order(60, 10, .10))
        test_price_over_fifty.assertEqual(58.56, coupon_calculations.calculate_order(75, 10, .15))
        test_price_over_fifty.assertEqual(59.36, coupon_calculations.calculate_order(80, 10, .20))
        test_price_over_fifty.assertEqual(59.62, coupon_calculations.calculate_order(85, 10, .25))
        test_price_over_fifty.assertEqual(59.36, coupon_calculations.calculate_order(90, 10, .30))
if __name__ == '__main__':
    unittest.main()
