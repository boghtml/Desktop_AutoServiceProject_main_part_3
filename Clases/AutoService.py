from collections import Counter
from collections import defaultdict
from datetime import datetime, timedelta

from Clases.CarOrder import CarOrder
from Clases.Service import Service
from Clases.signals import signals
from DataBase.DataBase import remove_order_base


class AutoService:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if AutoService._instance is not None:
            raise Exception("This class is a singleton!")
        self.cars = []
        self.employees = []
        self.orders = []
        self.services = []
        self.repair_costs = {}
        self.ordered_parts_history = {}

    def get_car_by_id(self, car_id):
        for car in self.cars:
            if str(car._id) == str(car_id):
                return car
        return None

    def get_service_by_id(self, service_id):
        for service in self.services:
            if str(service._id) == str(service_id):
                return service
        return None

    def add_service(self, service):
        self.services.append(service)

    def get_service_price(self, service_name):
        for service in self.services:
            if service.get_name() == service_name:
                return service.get_price()
        return None

    def get_services(self):
        return self.services

    def add_carToStart(self, car):
        self.cars.insert(0, car)

    def update_car(self, car):
        try:
            for i, c in enumerate(self.cars):
                if c._id == car._id:
                    self.cars[i] = car
                    break
        except Exception as e:
            print(e)

    def update_employee(self, employee):
        try:
            for emp in self.employees:
                if emp.get_id() == employee.get_id():
                    emp.name = employee.name
                    emp.position = employee.position
                    emp.salary = employee.salary
                    break
        except Exception as e:
            print(e)

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, index):
        if 0 <= index < len(self.cars):
            del self.cars[index]

    def addEmployee(self, employee):
        self.employees.append(employee)

    def removeEmployee(self, index):
        if 0 <= index < len(self.employees):
            del self.employees[index]

    def add_order(self, order):
        self.orders.append(order)

        signals.order_updated.emit()

    def add_orderToStart(self, order):
        self.orders.insert(0, order)

        # Викликаємо сигнал, щоб повідомити інші частини програми про оновлення
        signals.order_updated.emit()

    def get_orders(self):
        return self.orders

    def get_car_orders(self, car):
        car_orders = []
        for order in self.orders:
            if isinstance(order, CarOrder) and order.get_car() == car:
                car_orders.append(order)
        return car_orders

    def search_cars_by_brand(self, brand):
        return [car for car in self.cars if car.brand.lower() == brand.lower()]

    def sort_cars_by_year(self):
        return sorted(self.cars, key=lambda car: car.year)

    def searchEmployeesByName(self, name):
        return [employee for employee in self.employees if employee.name.lower() == name.lower()]

    def sort_employees_by_salary(self):
        return sorted(self.employees, key=lambda employee: employee.salary)

    def add_repair_cost(self, car, cost):
        if car in self.repair_costs:
            self.repair_costs[car] += cost
        else:
            self.repair_costs[car] = cost

    def order_part(self, car, part_name, cost):
        if car not in self.ordered_parts_history:
            self.ordered_parts_history[car] = []
        self.ordered_parts_history[car].append(part_name)
        self.add_repair_cost(car, cost)

    def get_cars(self):
        return self.cars

    def getEmployees(self):
        return self.employees

    def display_car_history(self, car):
        print("Історія замовлень:")
        for order in car.get_orders():
            print("-----------")
            print(order.get_order_details())

    def select_car_from_list(self):
        print("Оберіть автомобіль:")
        self.display_cars()
        if not self.cars:
            print("Немає доступних автомобілів.")
            return None
        try:
            car_index = int(input("Введіть номер автомобіля: ")) - 1
            if 0 <= car_index < len(self.cars):
                return self.cars[car_index]
            else:
                print("Невірний номер автомобіля.")
                return None
        except ValueError:
            print("Будь ласка, введіть число.")
            return None

    def display_cars(self):
        if self.cars:
            print("Список автомобілів:")
            for index, car in enumerate(self.cars, start=1):
                print(f"{index}) Марка: {car.brand}, Модель: {car.model}, Рік випуску: {car.year}")
        else:
            print("Немає інформації про автомобілі.")

    def get_service_by_name(self, name):
        for service in self.services:
            if service.name == name:
                return service
        return None

    def update_service(self, service):
        try:
            for i, s in enumerate(self.services):
                if s._id == service._id:
                    self.services[i] = service
                    break
        except Exception as e:
            print(e)

    def display_employees(self):
        print("Список працівників:")
        for index, employee in enumerate(self.employees, start=1):
            print(f"{index}) Ім'я: {employee.name}, Посада: {employee.position}, Зарплата: {employee.salary}")

    def display_ordered_parts(self):
        print("Замовлені запчастини:")
        for part in self.ordered_parts:
            print(part)

    def display_price_menu(self):
        # Тут може бути використано список або словник для зберігання і виводу пунктів меню
        price_menu = [
            "1) Заміна тормозних колодок - $500",
            # Додайте решту пунктів аналогічно
        ]
        print("Меню цін та ремонтів:")
        for item in price_menu:
            print(item)

    def remove_service(self, index):
        # Видаляємо послугу за індексом
        if 0 <= index < len(self.services):
            del self.services[index]

    def remove_order(self, order):
        # Якщо order є об'єктом замовлення
        if isinstance(order, CarOrder):
            # Видаляємо замовлення зі списку
            self.orders.remove(order)
            # Видаляємо замовлення з бази даних за його ID
            remove_order_base(order._id)

        signals.order_updated.emit()

    def get_number_of_cars(self):
        return len(self.cars)

    def get_number_of_employees(self):
        return len(self.employees)

    def get_number_of_services(self):
        return len(self.services)

    def get_number_of_orders(self):
        return len(self.orders)

    def get_employee_salaries(self):
        names = [employee.name for employee in self.employees]
        salaries = [employee.salary for employee in self.employees]
        return names, salaries

    def get_cars_count_by_brand(self):
        cars_count_by_brand = {}
        for car in self.cars:
            if car.brand in cars_count_by_brand:
                cars_count_by_brand[car.brand] += 1
            else:
                cars_count_by_brand[car.brand] = 1
        return cars_count_by_brand

    def get_cars_count_by_year(self):
        year_counts = {}
        for car in self.cars:
            if car.year in year_counts:
                year_counts[car.year] += 1
            else:
                year_counts[car.year] = 1
        years = list(year_counts.keys())
        counts = list(year_counts.values())
        years, counts = zip(*sorted(zip(years, counts)))  # Сортування за роком
        return years, counts

    def get_services_and_prices(self):
        services = [(service.name, service.price) for service in self.services]
        services.sort(key=lambda x: x[1])  # Сортування послуг за ціною
        return zip(*services)  # Розділення на два списки: назви та ціни

    def get_order_dynamics_by_date(self):
        try:
            current_month_start = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            next_month_start = (current_month_start + timedelta(days=32)).replace(day=1)

            dates = [order.date for order in self.orders if
                     current_month_start <= datetime.strptime(order.date, "%d-%m-%Y") < next_month_start]
            date_counts = Counter(dates)
            dates_sorted, counts_sorted = zip(
                *sorted(date_counts.items(), key=lambda x: datetime.strptime(x[0], "%d-%m-%Y")))
            return dates_sorted, counts_sorted
        except Exception as e:
            print(e)

    def get_revenue_by_date(self, filter_by='month'):
        current_date = datetime.now()
        revenue_by_date = defaultdict(float)

        for order in self.orders:
            date = datetime.strptime(order.date, "%d-%m-%Y")
            if filter_by == 'month' and (date.year == current_date.year and date.month == current_date.month):
                if order.cost <= 40000:
                    revenue_by_date[date] += order.cost
            elif filter_by == 'year' and date.year == current_date.year:
                if order.cost <= 40000:
                    revenue_by_date[date] += order.cost

        return revenue_by_date

    def get_service_distribution(self):
        service_counts = defaultdict(int)
        for order in self.orders:
            if hasattr(order, 'ordered_parts') and isinstance(order.ordered_parts, list):
                for service in order.ordered_parts:
                    # Переконуємося, що service є екземпляром Service, і використовуємо його назву
                    if isinstance(service, Service):
                        service_name = service.get_name()  # Припускаємо, що у Service є метод get_name()
                        service_counts[service_name] += 1
        return dict(service_counts)

    def get_order_values(self):
        return [order.cost for order in self.orders]
