from bson import ObjectId


class Car:
    def __init__(self, brand, model, year, _id=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.orders = []
        self._id = _id or ObjectId()

    def add_order(self, order):
        self.orders.append(order)

    def get_orders(self):
        return self.orders

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def __str__(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Рік випуску: {self.year}"

    def get_orders(self):
        return self.orders
