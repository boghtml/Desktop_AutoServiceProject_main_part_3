# В ClientManagementForm.py
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QCheckBox, QTableWidgetItem
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore
from Clases.AutoService import AutoService
from Clases.Car import Car
from Clases.signals import signals

from DataBase.DataBase import get_clients, get_clients1, delete_client, get_clients_by_phone, add_car_base, \
    update_client_viewed_status, get_client_by_id
from FormDesign.FormHandlers.ClientManagementForm_design import Ui_Form
from MainFunctionality.ChangingStatusForClientsForm import StatusChangeForm
from MainFunctionality.OrderMakingForm import OrderMakingForm


class ClientManagementForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.initializeUI()

        self.autoService = AutoService.get_instance()

        row_count = self.tableWidgetForOutputClients.rowCount()

        # Задаємо мінімальну висоту для кожного рядка
        for row in range(row_count):
            self.tableWidgetForOutputClients.setRowHeight(row, 75)

        self.tableWidgetForOutputClients.setColumnWidth(6, 135)
        self.tableWidgetForOutputClients.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        self.pushButtonForNewChecekdClients.setVisible(False)
        # Функціонал
        self.currentFilter = "Усі"

        self.update_client_data()
        # Після того, як ви додали дані до таблиці
        self.tableWidgetForOutputClients.resizeRowsToContents()
        self.tableWidgetForOutputClients.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        self.pushButton_ForAplyPrintingClients.clicked.connect(self.filterClients)
        self.pushButtonForAplyClients.clicked.connect(self.acceptClient)
        self.pushButtonForDenyClients.clicked.connect(self.denyClient)
        self.lineEditForSearchingClientsByNumber.textChanged.connect(self.searchClientsByPhone)
        self.pushButton_ForMakingOrderOnClient.clicked.connect(self.create_order_for_client)
        self.pushButtonForNewChecekdClients.clicked.connect(self.update_viewed_status)

        self.timer = QTimer(self)  # Створення таймера
        self.timer.timeout.connect(self.update_client_data)  # З'єднання сигналу timeout з методом оновлення
        self.timer.start(25000)  # Запуск таймера з інтервалом в 25000 мілісекунд (25 секунд)

        self.pushButton_ForUpdateDataAboutClient.clicked.connect(
            self.update_client_data)  # Призначення кнопки для ручного оновлення

        self.pushButton_ForChangingStatus.clicked.connect(self.on_pushButton_ForChangingStatus_clicked)

    def on_pushButton_ForChangingStatus_clicked(self):
        try:
            selected_row = self.tableWidgetForOutputClients.currentRow()
            if selected_row != -1:
                item = self.tableWidgetForOutputClients.item(selected_row, 10)  # Отримуємо QTableWidgetItem
                if item is not None:
                    client_id = item.data(QtCore.Qt.UserRole)  # Отримуємо дані
                    client = get_client_by_id(client_id)
                    if client:
                        dialog = StatusChangeForm(client)
                        if dialog.exec_() == QtWidgets.QDialog.Accepted:
                            self.loadClientsFromDB_1()
                    else:
                        QtWidgets.QMessageBox.warning(self, "Помилка", "Клієнта не знайдено в базі даних.")
                else:
                    QtWidgets.QMessageBox.warning(self, "Помилка", "Не вдалося отримати ID клієнта.")

            self.loadClientsFromDB_1()
        except Exception as e:
            print(f"Error: {e}")

    def update_client_data(self):
        self.loadClientsFromDB_1()
        self.update_not_viewed_count()
        self.fillComboBox()

    def update_viewed_status(self):
        try:
            for row in range(self.tableWidgetForOutputClients.rowCount()):
                check_box = self.tableWidgetForOutputClients.cellWidget(row, 8)
                client_id = check_box.property("client_id")
                new_viewed_status = check_box.isChecked()
                update_client_viewed_status(client_id, new_viewed_status)  # Оновлення бази даних

            self.pushButtonForNewChecekdClients.setVisible(False)
            self.loadClientsFromDB_1()  # Перезавантаження даних у таблиці
            self.update_not_viewed_count()  # Оновлення лічильника непереглянутих клієнтів
        except Exception as e:
            print(e)

    def update_not_viewed_count(self):
        try:
            not_viewed_count = 0
            for row in range(self.tableWidgetForOutputClients.rowCount()):
                check_box = self.tableWidgetForOutputClients.cellWidget(row, 8)  # Припустимо, що це дев'ятий стовпець
                if not check_box.isChecked():
                    not_viewed_count += 1
            self.label_ForPrintingCountOfNotChecked.setText(f"{not_viewed_count}")
            signals.new_clients_count_updated.emit(not_viewed_count)
        except Exception as e:
            print(e)

    def updateClientsTable(self, clients):
        self.tableWidgetForOutputClients.setRowCount(0)
        for client in clients:
            row_position = self.tableWidgetForOutputClients.rowCount()
            self.tableWidgetForOutputClients.insertRow(row_position)
            # Вказуємо поля явно

            self.tableWidgetForOutputClients.setItem(row_position, 0,
                                                     QtWidgets.QTableWidgetItem(client.get('name', '')))
            self.tableWidgetForOutputClients.setItem(row_position, 1,
                                                     QtWidgets.QTableWidgetItem(client.get('surname', '')))
            self.tableWidgetForOutputClients.setItem(row_position, 2,
                                                     QtWidgets.QTableWidgetItem(client.get('phone', '')))
            self.tableWidgetForOutputClients.setItem(row_position, 3,
                                                     QtWidgets.QTableWidgetItem(client.get('brand', '')))
            self.tableWidgetForOutputClients.setItem(row_position, 4,
                                                     QtWidgets.QTableWidgetItem(client.get('model', '')))
            self.tableWidgetForOutputClients.setItem(row_position, 5,
                                                     QtWidgets.QTableWidgetItem(client.get('year', '')))
            self.tableWidgetForOutputClients.setItem(row_position, 6,
                                                     QtWidgets.QTableWidgetItem(client.get('date', '')))
            self.tableWidgetForOutputClients.setItem(row_position, 7,
                                                     QtWidgets.QTableWidgetItem(
                                                         client.get('comment', '')))
            # Додаємо CheckBox для стовпця "Переглянуто"
            check_box = QCheckBox()
            check_box.setChecked(client.get('viewed', False))
            check_box.setProperty("client_id", client['_id'])  # Зберігаємо _id як властивість
            check_box.stateChanged.connect(self.onCheckBoxStateChanged)
            self.tableWidgetForOutputClients.setCellWidget(row_position, 8, check_box)

            self.tableWidgetForOutputClients.setItem(row_position, 9,
                                                     QtWidgets.QTableWidgetItem(client.get('status', 'Завершено')))

            id_item = QtWidgets.QTableWidgetItem()
            id_item.setData(QtCore.Qt.UserRole, str(client['_id']))
            self.tableWidgetForOutputClients.setItem(row_position, 10, id_item)

            # і так далі для інших полів

    def fillComboBox(self):
        try:
            self.comboBoxForChosingClients.clear()  # Очищення comboBox перед заповненням
            clients = get_clients()  # отримуємо список клієнтів з вашої БД
            if not clients:
                QMessageBox.information(self, "Немає клієнтів", "У базі даних немає жодного клієнта.")
            else:
                for client in reversed(clients):  # Використовуємо reversed для ітерації у зворотному порядку
                    client_info = f"{client['name']} - {client['phone']} - {client['date']}"
                    client_id = str(client["_id"])
                    self.comboBoxForChosingClients.addItem(client_info, client_id)
        except Exception as e:
            print(e)

    def acceptClient(self):
        client_id = self.comboBoxForChosingClients.currentData()
        if client_id:
            if delete_client(client_id):
                self.loadClientsFromDB()
                self.fillComboBox()
                QMessageBox.information(self, "Видалення", "Клієнт успішно видалений.")
            else:
                QMessageBox.warning(self, "Помилка", "Не вдалося видалити клієнта з бази даних.")
        else:
            QMessageBox.warning(self, "Помилка", "Не вдалося визначити ID клієнта для видалення.")

    def denyClient(self):
        client_id = self.comboBoxForChosingClients.currentData()
        if client_id:
            if delete_client(client_id):
                self.loadClientsFromDB()
                self.fillComboBox()
                QMessageBox.information(self, "Видалення", "Клієнт успішно видалений.")
            else:
                QMessageBox.warning(self, "Помилка", "Не вдалося видалити клієнта з бази даних.")
        else:
            QMessageBox.warning(self, "Помилка", "Не вдалося визначити ID клієнта для видалення.")

    def filterClients(self):
        try:
            self.currentFilter = self.comboBoxForChosingTypyOfPrintClients.currentText()
            self.loadClientsFromDB_1()
        except Exception as e:
            print(e)

    def loadClientsFromDB_1(self):
        try:
            self.tableWidgetForOutputClients.setRowCount(0)  # Очищення таблиці перед завантаженням нових даних
            filter_option = self.currentFilter
            clients = get_clients1(filter_option)  # отримуємо список клієнтів з вашої БД згідно з вибраним фільтром
            if not clients:
                QMessageBox.information(self, "Немає результатів",
                                        f"Немає клієнтів, що відповідають фільтру '{filter_option}'.")
            else:
                for client in reversed(clients):
                    row_position = self.tableWidgetForOutputClients.rowCount()
                    self.tableWidgetForOutputClients.insertRow(row_position)

                    # Вказуємо поля явно
                    self.tableWidgetForOutputClients.setItem(row_position, 0,
                                                             QtWidgets.QTableWidgetItem(client.get('name', '')))
                    self.tableWidgetForOutputClients.setItem(row_position, 1,
                                                             QtWidgets.QTableWidgetItem(client.get('surname', '')))
                    self.tableWidgetForOutputClients.setItem(row_position, 2,
                                                             QtWidgets.QTableWidgetItem(client.get('phone', '')))
                    self.tableWidgetForOutputClients.setItem(row_position, 3,
                                                             QtWidgets.QTableWidgetItem(client.get('brand', '')))
                    self.tableWidgetForOutputClients.setItem(row_position, 4,
                                                             QtWidgets.QTableWidgetItem(client.get('model', '')))
                    self.tableWidgetForOutputClients.setItem(row_position, 5,
                                                             QtWidgets.QTableWidgetItem(client.get('year', '')))
                    self.tableWidgetForOutputClients.setItem(row_position, 6,
                                                             QtWidgets.QTableWidgetItem(client.get('date', '')))
                    self.tableWidgetForOutputClients.setItem(row_position, 7,
                                                             QtWidgets.QTableWidgetItem(
                                                                 client.get('comment', '')))
                    check_box = QCheckBox()
                    check_box.setChecked(client.get('viewed', False))
                    check_box.setProperty("client_id", client['_id'])  # Зберігаємо _id як властивість
                    check_box.stateChanged.connect(self.onCheckBoxStateChanged)
                    self.tableWidgetForOutputClients.setCellWidget(row_position, 8, check_box)

                    self.tableWidgetForOutputClients.setItem(row_position, 9,
                                                             QtWidgets.QTableWidgetItem(
                                                                 client.get('status', 'Завершено')))
                    id_item = QtWidgets.QTableWidgetItem()
                    id_item.setData(QtCore.Qt.UserRole, str(client['_id']))
                    self.tableWidgetForOutputClients.setItem(row_position, 10, id_item)
        except Exception as e:
            print(e)

    def loadClientsFromDB(self):
        try:
            self.comboBoxForChosingClients.clear()  # Очищення comboBox перед заповненням
            clients = get_clients()  # отримуємо список клієнтів з вашої БД
            self.tableWidgetForOutputClients.setRowCount(0)  # Очищення таблиці перед заповненням

            for client in reversed(clients):
                row_position = self.tableWidgetForOutputClients.rowCount()
                self.tableWidgetForOutputClients.insertRow(row_position)

                self.tableWidgetForOutputClients.setItem(row_position, 0,
                                                         QtWidgets.QTableWidgetItem(client.get('name', '')))
                self.tableWidgetForOutputClients.setItem(row_position, 1,
                                                         QtWidgets.QTableWidgetItem(client.get('surname', '')))
                self.tableWidgetForOutputClients.setItem(row_position, 2,
                                                         QtWidgets.QTableWidgetItem(client.get('phone', '')))
                self.tableWidgetForOutputClients.setItem(row_position, 3,
                                                         QtWidgets.QTableWidgetItem(client.get('brand', '')))
                self.tableWidgetForOutputClients.setItem(row_position, 4,
                                                         QtWidgets.QTableWidgetItem(client.get('model', '')))
                self.tableWidgetForOutputClients.setItem(row_position, 5,
                                                         QtWidgets.QTableWidgetItem(client.get('year', '')))
                self.tableWidgetForOutputClients.setItem(row_position, 6,
                                                         QtWidgets.QTableWidgetItem(client.get('date', '')))
                self.tableWidgetForOutputClients.setItem(row_position, 7,
                                                         QtWidgets.QTableWidgetItem(
                                                             client.get('comment', '')))
                check_box = QCheckBox()
                check_box.setChecked(client.get('viewed', False))
                check_box.setProperty("client_id", client['_id'])  # Зберігаємо _id як властивість
                check_box.stateChanged.connect(self.onCheckBoxStateChanged)
                self.tableWidgetForOutputClients.setCellWidget(row_position, 8, check_box)

                self.tableWidgetForOutputClients.setItem(row_position, 9,
                                                         QtWidgets.QTableWidgetItem(
                                                             client.get('status', 'Завершено')))
                # Додаємо id як користувальницьку роль у перший стовпець
                id_item = QtWidgets.QTableWidgetItem()
                id_item.setData(QtCore.Qt.UserRole, str(client['_id']))
                self.tableWidgetForOutputClients.setItem(row_position, 10, id_item)


        except Exception as e:
            print(e)

    def create_order_for_client(self):
        try:
            selected_row = self.tableWidgetForOutputClients.currentRow()
            if selected_row >= 0:
                brand = self.tableWidgetForOutputClients.item(selected_row, 3).text()
                model = self.tableWidgetForOutputClients.item(selected_row, 4).text()
                year = self.tableWidgetForOutputClients.item(selected_row, 5).text()

                # Створення нового автомобіля та додавання його до CarManagementForm
                car = Car(brand, model, int(year))
                try:
                    result = add_car_base(car)
                    car._id = result.inserted_id
                    self.autoService.add_carToStart(car)
                    signals.car_added.emit()
                except Exception as e:
                    QMessageBox.critical(self, "Помилка додавання", str(e))

                # Відкриття форми замовлення
                self.order_making_form = OrderMakingForm()
                self.order_making_form.comboBoxForChosingCars.setCurrentIndex(self.autoService.get_cars().index(car))
                self.order_making_form.show()
            else:
                QMessageBox.warning(self, 'Помилка', 'Будь ласка, виберіть клієнта.')

            signals.order_making_client.emit()
        except Exception as e:
            print(e)

    def searchClientsByPhone(self):
        try:
            phone_number = self.lineEditForSearchingClientsByNumber.text().strip()
            if phone_number:
                clients = get_clients_by_phone(phone_number)
                self.updateClientsTable(clients)
            else:
                self.loadClientsFromDB_1()
                self.fillComboBox()
        except Exception as e:
            print(e)

    def onCheckBoxStateChanged(self, state):
        self.pushButtonForNewChecekdClients.setVisible(True)

    def initializeUI(self):
        self.tableWidgetForOutputClients.setToolTip("Таблиця з даними про клієнтів")
        self.comboBoxForChosingTypyOfPrintClients.setToolTip("Виберіть спосіб виведення клієнтів")
        self.pushButton_ForAplyPrintingClients.setToolTip("Натисніть для виведення клієнтів згідно фільрів")
        self.comboBoxForChosingClients.setToolTip("Виберіть клієнта для виконання дій даних")
        self.pushButtonForAplyClients.setToolTip("Натисніть для винонання роботи із клієнтом")
        self.pushButtonForDenyClients.setToolTip("Натисніть для видалення даних про клієнта")
        self.lineEditForSearchingClientsByNumber.setToolTip("Введіть номер телефону для пошуку клієнта")
        self.pushButton_ForMakingOrderOnClient.setToolTip("Натисніть для створення замовлення для вибраного клієнта")
        self.pushButtonForNewChecekdClients.setToolTip("Натисніть для застосування chaeck для клієнтів")
        self.pushButton_ForUpdateDataAboutClient.setToolTip("Натисніть для оновлення даних про клієнтів")
        self.pushButton_ForChangingStatus.setToolTip(
            "Натисніть на працівника в табличці\n та натисніть цю кнопку для зміни статусу вибраного клієнта")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainForm = ClientManagementForm()
    mainForm.show()
    sys.exit(app.exec_())
