class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price
        }

    @staticmethod
    def from_dict(data):
        return Product(
            product_id=data['product_id'],
            name=data['name'],
            price=data['price']
        )