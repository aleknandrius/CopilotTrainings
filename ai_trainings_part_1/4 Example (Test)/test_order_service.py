import unittest
from order_service import OrderService

class TestOrderService(unittest.TestCase):

    def setUp(self):
        self.service = OrderService()
        self.sample_products = [{'id': 1, 'price': 100.0}, {'id': 2, 'price': 200.0}]
        self.sample_quantities = {1: 2, 2: 1}

    def test_create_order_without_coupon(self):
        order = self.service.create_order(self.sample_products, self.sample_quantities)
        self.assertEqual(len(order['items']), 2)
        self.assertEqual(order['total_price'], 400.0)
        self.assertEqual(order['items'][0]['line_price'], 200.0)
        self.assertEqual(order['items'][1]['line_price'], 200.0)

    def test_create_order_with_coupon(self):
        order = self.service.create_order(self.sample_products, self.sample_quantities, coupon_code='SUMMER2025')
        self.assertEqual(len(order['items']), 2)
        self.assertEqual(order['total_price'], 320.0)
        self.assertEqual(order['items'][0]['line_price'], 200.0)
        self.assertEqual(order['items'][1]['line_price'], 200.0)

    def test_create_order_with_default_quantity(self):
        sample_quantities = {1: 2}  # Only quantity for product 1 is provided
        order = self.service.create_order(self.sample_products, sample_quantities)
        self.assertEqual(len(order['items']), 2)
        self.assertEqual(order['items'][0]['qty'], 2)
        self.assertEqual(order['items'][1]['qty'], 1)  # Default quantity should be 1
        self.assertEqual(order['total_price'], 400.0)

if __name__ == '__main__':
    unittest.main()