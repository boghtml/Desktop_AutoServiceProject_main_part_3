from abc import ABC, abstractmethod

class Order(ABC):
    def __init__(self, cost, date):
        self.cost = cost
        self.date = date

    def get_cost(self):
        return self.cost

    def get_date(self):
        return self.date

    @abstractmethod
    def get_order_details(self):
        pass
