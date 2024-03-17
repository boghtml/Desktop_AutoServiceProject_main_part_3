import sys

from PyQt5 import QtCore, QtWidgets

from Calses.AutoService import AutoService
from Calses.Car import Car
from Calses.CarOrder import CarOrder
from Calses.Employee import Employee
from Calses.Service import Service
from DataBase_trial.DataBase import get_orders_base, get_cars_base, get_employees_base, get_services_base
from FormDesign.SplashScreenForm_design import Ui_SplashScreen  # Правильний шлях до вашого UI класу


class SplashScreenForm(QtWidgets.QMainWindow, Ui_SplashScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.progressBar.setValue(0)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.advanceProgressBar)
        self.timer.start(75)

        self.autoService = AutoService.get_instance()
        self.initialization()

    def advanceProgressBar(self):
        current_value = self.progressBar.value()
        max_value = self.progressBar.maximum()

        # Оновлюємо текст в label_description відповідно до прогресу
        if current_value < max_value // 3:
            self.label_description.setText("Завантаження ресурсів...")
        elif current_value < 2 * max_value // 3:
            self.label_description.setText("Ініціалізація модулів...")
        else:
            self.label_description.setText("Фіналізація налаштувань...")

        if current_value < max_value:
            self.progressBar.setValue(current_value + 1)
        else:
            self.timer.stop()  # Зупиняємо таймер, коли досягнуто максимуму
            self.openLoginForm()  # Відкриваємо форму авторизації

    def openLoginForm(self):
        # Імпортуйте і відкрийте вашу форму авторизації тут
        from LoginForm import Autorization  # Припускаємо, що у вас є такий клас
        self.login_form = Autorization()
        self.login_form.show()
        self.close()  # Закриваємо форму завантаження

    def initialization(self):

        self.initializeCarsFromDB()
        self.initializeEmpoyeeFromDB()
        self.initializeServicesFromDB()

        try:
            self.initializeOrdersFromDB()
        except Exception as e:
            print(e)

    def initializeOrdersFromDB(self):
        if not self.autoService.get_orders():
            orders_from_db = get_orders_base()  # отримати всі замовлення з бази даних
            for order_data in orders_from_db:
                car = self.autoService.get_car_by_id(order_data['car_id'])  # отримати авто за ID
                services = [self.autoService.get_service_by_id(service_id) for service_id in
                            order_data['services']]  # отримати послуги за ID

                if car and all(services):  # перевірка чи всі об'єкти були успішно отримані
                    print("Інформація про читання:", order_data['cost'], order_data['date'], car, services,
                          order_data['_id'])
                    new_order = CarOrder(order_data['cost'], order_data['date'], car, services, order_data['_id'])
                    self.autoService.add_order(new_order)  # додати замовлення до AutoService

    def initializeCarsFromDB(self):
        if not self.autoService.get_cars():  # Перевірка на відсутність автомобілів
            cars_from_db = get_cars_base()
            for car_data in cars_from_db:
                try:
                    car = Car(car_data['brand'], car_data['model'], car_data['year'], car_data['_id'])
                    self.autoService.add_car(car)
                except Exception as e:
                    print(e)

    def initializeEmpoyeeFromDB(self):
        if not self.autoService.getEmployees():
            employees_from_db = get_employees_base()  # Отримуємо список працівників з бази даних
            for emp_data in employees_from_db:
                # Створюємо екземпляри класу Employee на основі даних з бази даних
                employee = Employee(emp_data['name'], emp_data['position'], emp_data['salary'], emp_data['_id'])
                if not any(emp for emp in self.autoService.getEmployees() if
                           emp.get_name() == employee.get_name() and emp.get_position() == employee.get_position()):
                    self.autoService.addEmployee(employee)  # Додаємо працівника до AutoService, якщо він унікальний

    def initializeServicesFromDB(self):
        if not self.autoService.get_services():
            services_from_db = get_services_base()
            for service_data in services_from_db:
                service = Service(service_data['name'], service_data['price'], service_data['_id'])
                self.autoService.add_service(service)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    splashScreen = SplashScreenForm()
    splashScreen.show()
    sys.exit(app.exec_())
