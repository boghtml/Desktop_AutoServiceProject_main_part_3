from bson import ObjectId

from Clases.Order import Order


class CarOrder(Order):
    def __init__(self, cost, date, car, ordered_parts, comment=None, _id=None):
        super().__init__(cost, date)
        self.car = car
        self.ordered_parts = ordered_parts
        self.comment = comment
        self._id = _id or ObjectId()

    def to_dict(self):
        return {
            "cost": self.cost,
            "date": self.date,
            "car_id": self.car._id if hasattr(self.car, '_id') else None,
            "services": [service._id for service in self.ordered_parts if hasattr(service, '_id')],
            "comment": self.comment
        }

    def get_order_details(self):
        details = f"Замовлення для автомобіля:\nМарка: {self.car.get_brand()}, Модель: {self.car.get_model()}, Рік випуску: {self.car.get_year()}\nЗамовлені запчастини:\n"
        details += "\n".join(self.ordered_parts)
        details += f"\nЗагальна вартість: {self.get_cost()}\nДата виконання: {self.get_date()}\n"
        return details

    def get_car(self):
        return self.car

    def get_ordered_parts(self):
        return self.ordered_parts

    def get_ordered_services_names(self):
        return [service.get_name() for service in self.ordered_parts]

        # Getter and setter for comment

    def get_comment(self):
        return self.comment

    def set_comment(self, comment):
        self.comment = comment
