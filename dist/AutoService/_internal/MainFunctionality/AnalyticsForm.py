from datetime import datetime

import matplotlib.dates as mdates
from PyQt5 import QtWidgets
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator

from Clases.AutoService import AutoService
from FormDesign.FormHandlers.AnalyticsForm_design import Ui_Form


class AnalyticsForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.initializeUI()

        self.autoService = AutoService.get_instance()
        # self.initialization()
        # Створення Figure для графіків
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Додавання canvas як дочірній елемент до QWidget
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        self.widget_ForOutpurGraphs.setLayout(layout)  # yourQWidget це ваш QWidget на формі

        self.pushButtonForOutputGraphs.clicked.connect(self.outputGraph)

        self.comboBoxForSelectGraphs.addItems([
            "Кількість авто, працівників, послуг, замовлень",
            "Кількість авто за маркою",
            "Кількість авто за роком випуску",
            "Доходи працівників",
            "Графік для відображення послуг до їх вартості ціни",
            "Динаміка замовлень по даті",
            "Лінійний графік доходів від ремонтів за часом",
            "Пирогова діаграма розподілу послуг за частотою замовлень"
        ])

    def outputGraph(self):
        chosen_graph = self.comboBoxForSelectGraphs.currentText()

        if chosen_graph == "Кількість авто, працівників, послуг, замовлень":
            self.plot_general_statistics()
        elif chosen_graph == "Кількість авто за маркою":
            self.plot_cars_by_brand()
        elif chosen_graph == "Кількість авто за роком випуску":
            self.plot_cars_count_by_year()
        elif chosen_graph == "Доходи працівників":
            self.plot_employee_salaries()
        elif chosen_graph == "Графік для відображення послуг до їх вартості ціни":
            self.plot_services_and_prices()
        elif chosen_graph == "Динаміка замовлень по даті":
            self.plot_order_dynamics_by_date()
        elif chosen_graph == "Лінійний графік доходів від ремонтів за часом":
            self.plot_revenue_by_time()
        elif chosen_graph == "Пирогова діаграма розподілу послуг за частотою замовлень":
            self.plot_service_distribution()

    def plot_service_distribution(self):
        service_counts = self.autoService.get_service_distribution()
        services, counts = zip(*sorted(service_counts.items(), key=lambda item: item[1], reverse=True))

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Кастомізація кольорів
        colors = plt.cm.tab20c.colors  # Використовуємо колірну палітру matplotlib

        # Виділення сегментів
        explode = [0.1 if i == 0 else 0 for i in range(len(services))]  # Виділяємо перший сегмент

        wedges, texts, autotexts = ax.pie(counts, labels=services, autopct='%1.1f%%', startangle=140, colors=colors,
                                          explode=explode, shadow=True)

        # Кастомізація тексту
        for text in texts + autotexts:
            text.set_color('black')
        for autotext in autotexts:
            autotext.set_size('x-small')

        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title('Розподіл послуг за частотою замовлень', fontsize=14)

        # Додавання легенди
        # ax.legend(wedges, services, title="Послуги", loc="center left", bbox_to_anchor=(1, 0.5), fontsize='small')

        self.canvas.draw()

    def plot_revenue_by_time(self, filter_by='month'):
        revenue_by_date = self.autoService.get_revenue_by_date(filter_by)
        dates, revenues = zip(*sorted(revenue_by_date.items()))

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        ax.plot(dates, revenues, marker='o', linestyle='-', color='skyblue', label='Доходи від ремонтів')
        ax.legend()

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(True, linestyle='--', alpha=0.7)

        ax.tick_params(axis='x', labelrotation=45, labelsize=8)
        ax.tick_params(axis='y', labelsize=8)

        ax.set_title('Доходи від ремонтів за часом', fontsize=16)
        ax.set_xlabel('Дата', fontsize=12)
        ax.set_ylabel('Доходи', fontsize=12)

        if filter_by == 'month':
            ax.xaxis.set_major_locator(mdates.DayLocator())
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))
        elif filter_by == 'year':
            ax.xaxis.set_major_locator(mdates.MonthLocator())
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))

        self.figure.autofmt_xdate()
        self.canvas.draw()

    def plot_order_dynamics_by_date(self):
        dates, counts = self.autoService.get_order_dynamics_by_date()
        # Перетворення строкових дат у datetime
        dates = [datetime.strptime(date, "%d-%m-%Y") for date in dates]

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        ax.plot(dates, counts, marker='o', linestyle='-', color='skyblue', label='Кількість замовлень')
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_title("Динаміка замовлень по даті", fontsize=16)
        ax.set_xlabel("Дата", fontsize=12)
        ax.set_ylabel("Кількість замовлень", fontsize=12)

        # Встановлення локатора та форматтера для осі X
        ax.xaxis.set_major_locator(mdates.DayLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))

        self.figure.autofmt_xdate()
        self.canvas.draw()

    def plot_services_and_prices(self):
        service_names, prices = self.autoService.get_services_and_prices()

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        bars = ax.bar(service_names, prices, color='skyblue')

        for bar in bars:
            yval = round(bar.get_height(), 2)
            ax.text(bar.get_x() + bar.get_width() / 2, yval, str(yval), ha='center', va='bottom', fontsize=8)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_facecolor('whitesmoke')

        ax.tick_params(axis='x', rotation=30, labelsize=8)

        ax.tick_params(axis='y', labelsize=8)

        ax.yaxis.grid(True, linestyle='--', alpha=0.7)

        ax.set_title("Вартість послуг", fontsize=16)
        ax.set_xlabel("Послуги", fontsize=12)
        ax.set_ylabel("Ціна", fontsize=12)

        self.canvas.draw()

    def plot_cars_count_by_year(self):
        # Отримання даних
        years, counts = self.autoService.get_cars_count_by_year()

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        bars = ax.bar(years, counts, color='skyblue')

        for bar in bars:
            yval = round(bar.get_height())
            ax.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_facecolor('whitesmoke')
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        ax.set_title("Кількість авто за роком випуску", fontsize=16)
        ax.set_xlabel("Рік випуску", fontsize=12)
        ax.set_ylabel("Кількість авто", fontsize=12)

        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        self.canvas.draw()

    def plot_employee_salaries(self):
        names, salaries = self.autoService.get_employee_salaries()

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        ax.plot(names, salaries, marker='o', linestyle='-', color='lightgreen')

        ax.set_facecolor('whitesmoke')
        ax.set_title("Доходи працівників", fontsize=16)
        ax.set_xlabel("Працівники", fontsize=12)
        ax.set_ylabel("Дохід", fontsize=12)
        ax.grid(True)

        self.canvas.draw()

    def plot_cars_by_brand(self):
        cars_count_by_brand = self.autoService.get_cars_count_by_brand()

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        brands = list(cars_count_by_brand.keys())
        counts = list(cars_count_by_brand.values())
        bars = ax.bar(brands, counts, color='skyblue')

        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

        ax.set_facecolor('whitesmoke')
        ax.set_title("Кількість авто за марками", fontsize=16)
        ax.set_xlabel("Марки", fontsize=12)
        ax.set_ylabel("Кількість", fontsize=12)

        self.canvas.draw()

    def plot_general_statistics(self):
        num_cars = self.autoService.get_number_of_cars()
        num_employees = self.autoService.get_number_of_employees()
        num_services = self.autoService.get_number_of_services()
        num_orders = self.autoService.get_number_of_orders()

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon']

        bars = ax.bar(["Авто", "Працівники", "Послуги", "Замовлення"],
                      [num_cars, num_employees, num_services, num_orders], color=colors)

        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_facecolor('whitesmoke')

        ax.set_title("Загальна статистика", fontsize=16)
        ax.set_xlabel("Категорії", fontsize=12)
        ax.set_ylabel("Кількість", fontsize=12)

        self.canvas.draw()

    def initializeUI(self):
        self.comboBoxForSelectGraphs.setToolTip("Виберіть тип графіка для виведення")
        self.pushButtonForOutputGraphs.setToolTip("Натисніть для виведення вибраного графіка")
        self.widget_ForOutpurGraphs.setToolTip("Область для виведення графіків")


'''def initialization(self):

        self.initializeCarsFromDB()
        self.initializeEmpoyeeFromDB()
        self.initializeServicesFromDB()

        try:
            self.initializeOrdersFromDB()
        except Exception as e:
            print(e)

    def initializeOrdersFromDB(self):
        if not self.autoService.get_orders():
            orders_from_db = get_orders_base()
            for order_data in orders_from_db:
                car = self.autoService.get_car_by_id(order_data['car_id'])  # отримати авто за ID
                services = [self.autoService.get_service_by_id(service_id) for service_id in
                            order_data['services']]

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

    '''
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = AnalyticsForm()
    window.show()
    sys.exit(app.exec_())
