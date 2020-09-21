"""
Morgan Christensen

Module 4 - Nested if statements

09/21/20
"""


def calculate_order(price, cash_coupon, percent_coupon):
    TAX = .06
    total_coupon1 = (float(price) - float(cash_coupon))
    total_coupons = total_coupon1 - (total_coupon1 * float(percent_coupons))
    total_tax = total_coupons + (total_coupons * TAX)
    if total_coupons >= 50:
        return total_tax
    elif total_coupons >= 30:
        shipping_cost = 11.95
        total = total_tax + shipping_cost
        return total
    elif total_coupons >= 10:
        shipping_cost = 7.95
        total = total_tax + shipping_cost
        return total
    else:
        shipping_cost = 5.95
        total = total_tax + shipping_cost
        return total


if __name__ == '__main__':
    price = input("What is the total price of your purchase? ")
    cash_coupons = input("If you have any cash coupons enter their amount (5 or 10) else enter 0: ")
    percent_coupons = input("If you have any percentage coupons enter their decimal otherwise enter 0: ")
    print("The total amount of your purchase after coupons, tax, and shipping is {}".format(calculate_order(price, cash_coupons, percent_coupons)))
