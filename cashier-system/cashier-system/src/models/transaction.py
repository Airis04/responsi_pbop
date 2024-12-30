class Transaction:
    def __init__(self, product_name, quantity, total_price, date):
        self.product_name = product_name
        self.quantity = quantity
        self.total_price = total_price
        self.date = date

    def __str__(self):
        return f"Transaction({self.product_name}, Quantity: {self.quantity}, Total Price: {self.total_price}, Date: {self.date})"

    def to_dict(self):
        return {
            "product_name": self.product_name,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "date": self.date
        }