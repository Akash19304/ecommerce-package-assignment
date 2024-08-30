# tests/test_product_management.py

import unittest
from ecommerce.products.product_management import Product, Inventory

class TestProductManagement(unittest.TestCase):

    def test_add_product(self):
        inventory = Inventory()
        product = Product("Laptop", 1000, 10)
        inventory.add_product(product)
        self.assertEqual(len(inventory.products), 1)

    def test_update_quantity(self):
        product = Product("Laptop", 1000, 10)
        product.update_quantity(5)
        self.assertEqual(product.quantity, 5)

if __name__ == '__main__':
    unittest.main()
