from PyQt5 import QtWidgets

from Clases.AutoService import AutoService
from FormDesign.FormHandlers.DetailedServiceForm_design import Ui_Form  # Імпортуйте ваш UI клас

from Clases.signals import signals
import datetime


class DetailedOrderForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(DetailedOrderForm, self).__init__()
        self.setupUi(self)

        self.initializeUI()

        self.autoService = AutoService.get_instance()
        self.selected_services = []

        self.tableWidgetForOutputOrders.setColumnWidth(1, 225)

        self.comboBoxForSortOrders.addItem("Звичайний порядок", "normal")
        self.comboBoxForSortOrders.addItem("За ціною", "price")
        self.comboBoxForSortOrders.addItem("За датою", "date")
        self.comboBoxForSortOrders.addItem("За кількістю послуг", "services_count")

        self.comboBoxForDataOutputOrders.addItem("За сьогодні", "today")
        self.comboBoxForDataOutputOrders.addItem("Попередній тиждень", "last_week")
        self.comboBoxForDataOutputOrders.addItem("Місяць", "last_month")
        self.comboBoxForDataOutputOrders.addItem("Рік", "last_year")
        self.comboBoxForDataOutputOrders.addItem("За весь час", "all_time")

        # Тут можна додати додаткову ініціалізацію

        self.pushButtonForAplyDataQuery.clicked.connect(self.displayData)
        self.pushButtonForDeleteOrder.clicked.connect(self.deleteOrder)

        try:
            self.pushButton_ForAplySort.clicked.connect(self.sortOrders)
        except Exception as e:
            print(e)

        signals.order_updated.connect(self.updateOrderTable1)

        try:
            self.updateOrderTable1()
        except Exception as e:
            print(e)

        self.tableWidgetForOutputOrders.setHorizontalHeaderLabels(
            ["Авто", "Послуги", "Ціна", "Дата", "Коментар"])

    def displayData(self):
        filter_option = self.comboBoxForDataOutputOrders.currentData()
        today = datetime.date.today()

        # Для минулого року
        first_day_of_last_year = datetime.date(today.year - 1, 1, 1)
        last_day_of_last_year = datetime.date(today.year - 1, 12, 31)

        if filter_option == "today":
            filtered_orders = [order for order in self.autoService.get_orders() if
                               order.date == today.strftime("%d-%m-%Y")]
        elif filter_option == "last_week":
            one_week_ago = today - datetime.timedelta(weeks=1)
            filtered_orders = [order for order in self.autoService.get_orders() if
                               one_week_ago <= datetime.datetime.strptime(order.date, "%d-%m-%Y").date() <= today]
        elif filter_option == "last_month":
            first_day_of_current_month = datetime.date(today.year, today.month, 1)
            first_day_of_last_month = first_day_of_current_month - datetime.timedelta(days=1)
            first_day_of_last_month = datetime.date(first_day_of_last_month.year, first_day_of_last_month.month, 1)
            last_day_of_last_month = first_day_of_current_month - datetime.timedelta(days=1)
            filtered_orders = [order for order in self.autoService.get_orders() if
                               first_day_of_last_month <= datetime.datetime.strptime(order.date,
                                                                                     "%d-%m-%Y").date() <= last_day_of_last_month]
        elif filter_option == "last_year":
            filtered_orders = [order for order in self.autoService.get_orders() if
                               first_day_of_last_year <= datetime.datetime.strptime(order.date,
                                                                                    "%d-%m-%Y").date() <= last_day_of_last_year]
        elif filter_option == "all_time":
            filtered_orders = self.autoService.get_orders()

        self.displayFilteredOrders(filtered_orders)

    def displayFilteredOrders(self, orders):
        self.tableWidgetForOutputOrders.clearContents()
        self.tableWidgetForOutputOrders.setRowCount(0)
        for order in orders:
            self.addOrderToTable(order)  # використовуйте ваш існуючий метод для додавання замовлень у таблицю

    def deleteOrder(self):
        current_index = self.comboBoxChosingOrderDelete.currentIndex()
        if current_index < 0:
            QtWidgets.QMessageBox.warning(self, "Помилка", "Будь ласка, виберіть замовлення для видалення.")
            return

        # Отримуємо ID замовлення для видалення
        order_id_to_delete = self.comboBoxChosingOrderDelete.itemData(current_index)
        if order_id_to_delete:
            # Видаляємо замовлення з AutoService та бази даних
            self.autoService.remove_order(order_id_to_delete)
            self.updateOrderTable1()  # Оновлюємо таблицю та comboBox

    def updateOrderTable1(self):
        self.tableWidgetForOutputOrders.clear()
        self.tableWidgetForOutputOrders.setRowCount(0)
        self.comboBoxChosingOrderDelete.clear()  # Очищаємо comboBox перед оновленням

        orders = self.autoService.get_orders()
        for order in orders:
            row_position = self.tableWidgetForOutputOrders.rowCount()
            self.tableWidgetForOutputOrders.insertRow(row_position)

            car_info = f"{order.car.get_brand()} {order.car.get_model()} {order.car.get_year()}"
            services_names = ", ".join(order.get_ordered_services_names())
            order_info = f"{order.date} - {car_info} - {str(order.cost)}"  # Форматуємо інформацію для відображення в comboBox

            self.tableWidgetForOutputOrders.setItem(row_position, 0, QtWidgets.QTableWidgetItem(car_info))
            self.tableWidgetForOutputOrders.setItem(row_position, 1, QtWidgets.QTableWidgetItem(services_names))
            self.tableWidgetForOutputOrders.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(order.cost)))
            self.tableWidgetForOutputOrders.setItem(row_position, 3, QtWidgets.QTableWidgetItem(order.date))
            self.tableWidgetForOutputOrders.setItem(row_position, 4, QtWidgets.QTableWidgetItem(
                order.get_comment() or ""))

            self.comboBoxChosingOrderDelete.addItem(order_info, order)

    def sortOrders(self):
        sort_option = self.comboBoxForSortOrders.currentData()

        if sort_option == "normal":
            self.updateOrderTable1()
        else:
            orders = self.autoService.get_orders()
            try:
                if sort_option == "price":
                    sorted_orders = sorted(orders, key=lambda order: order.cost, reverse=True)
                elif sort_option == "date":
                    sorted_orders = sorted(orders, key=lambda x: datetime.datetime.strptime(x.date, "%d-%m-%Y"),
                                           reverse=True)
                elif sort_option == "services_count":
                    sorted_orders = sorted(orders, key=lambda order: len(order.get_ordered_services_names()),
                                           reverse=True)
            except Exception as e:
                print(e)

            self.displaySortedOrders(sorted_orders)

    def displaySortedOrders(self, sorted_orders):
        self.tableWidgetForOutputOrders.clearContents()
        self.tableWidgetForOutputOrders.setRowCount(0)

        for order in sorted_orders:
            try:
                self.addOrderToTable(order)
            except Exception as e:
                print(e)

    def addOrderToTable(self, order):
        row_position = self.tableWidgetForOutputOrders.rowCount()
        self.tableWidgetForOutputOrders.insertRow(row_position)

        # Формуємо інформацію про авто для відображення
        car_info = f"{order.car.get_brand()} {order.car.get_model()} {order.car.get_year()}"

        # Використовуємо правильний атрибут для отримання послуг
        services_names = ", ".join([service.get_name() for service in order.ordered_parts])

        # Додаємо інформацію до відповідних стовпців
        self.tableWidgetForOutputOrders.setItem(row_position, 0, QtWidgets.QTableWidgetItem(car_info))
        self.tableWidgetForOutputOrders.setItem(row_position, 1, QtWidgets.QTableWidgetItem(services_names))
        self.tableWidgetForOutputOrders.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(order.cost)))
        self.tableWidgetForOutputOrders.setItem(row_position, 3, QtWidgets.QTableWidgetItem(order.date))
        self.tableWidgetForOutputOrders.setItem(row_position, 4, QtWidgets.QTableWidgetItem(
            order.get_comment() or ""))

    def initializeUI(self):
        self.comboBoxForSortOrders.setToolTip("Виберіть спосіб сортування замовлень")
        self.tableWidgetForOutputOrders.setToolTip("Таблиця з замовленнями")
        self.comboBoxForDataOutputOrders.setToolTip("Виберіть період для виведення замовлень")
        self.pushButtonForAplyDataQuery.setToolTip("Натисніть, щоб вивести замовлення за вибраним періодом")
        self.pushButtonForDeleteOrder.setToolTip("Натисніть, щоб видалити вибране замовлення")
        self.pushButton_ForAplySort.setToolTip("Натисніть, щоб посортувати замовлення")
        self.comboBoxChosingOrderDelete.setToolTip("Виберіть замовлення для видалення")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = DetailedOrderForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
