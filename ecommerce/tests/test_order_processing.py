# tests/test_order_processing.py

import unittest
from ecommerce.products.product_management import Product
from ecommerce.orders.order_processing import Order

class TestOrderProcessing(unittest.TestCase):

    def test_process_order(self):
        product = Product("Laptop", 1000, 10)
        order = Order(1, product, 5)
        order.process_order()
        self.assertEqual(order.status, "Completed")
        self.assertEqual(product.quantity, 5)

if __name__ == '__main__':
    unittest.main()
