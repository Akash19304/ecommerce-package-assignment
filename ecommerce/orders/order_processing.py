# ecommerce/orders/order_processing.py

class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.status = "Pending"

    def process_order(self):
        if self.quantity <= self.product.quantity:
            self.product.update_quantity(self.product.quantity - self.quantity)
            self.status = "Completed"
        else:
            self.status = "Failed - Insufficient Stock"

    def get_order_details(self):
        return {
            "order_id": self.order_id,
            "product_name": self.product.name,
            "quantity": self.quantity,
            "status": self.status
        }
