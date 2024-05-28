from bson import ObjectId


class Service:
    def __init__(self, name, price, _id=None):
        self.name = name
        self.price = price
        self._id = _id or ObjectId()

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price
