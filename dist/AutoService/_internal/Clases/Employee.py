from bson import ObjectId


class Employee:
    def __init__(self, name, position, salary, _id=None):
        self.name = name
        self.position = position
        self.salary = salary
        self._id = _id or ObjectId()

    def get_id(self):
        return self._id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def __str__(self):
        return f"Ім'я: {self.name}, Посада: {self.position}, Зарплата: {self.salary:.2f}"
