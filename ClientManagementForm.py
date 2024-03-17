# В ClientManagementForm.py
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from DataBase_trial.DataBase import get_clients, get_clients1, delete_client
from FormDesign.ClientManegementForm_design import Ui_Form


class ClientManagementForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Ініціалізація UI без префікса ui

        self.currentFilter = "Усі"

        self.loadClientsFromDB()
        self.fillComboBox()

        self.pushButton_ForAplyPrintingClients.clicked.connect(self.filterClients)
        self.pushButtonForAplyClients.clicked.connect(self.acceptClient)
        self.pushButtonForDenyClients.clicked.connect(self.denyClient)

    def fillComboBox(self):
        try:
            self.comboBoxForChosingClients.clear()  # Очищення comboBox перед заповненням
            clients = get_clients()  # отримуємо список клієнтів з вашої БД
            for client in clients:
                client_info = f"{client['name']} - {client['phone']} - {client['date']}"
                print("Інформація - " + client_info)
                client_id = str(client["_id"])  # Переконайтеся, що використовуєте str для конвертації ObjectId у рядок
                print("Id - " + client_id)
                self.comboBoxForChosingClients.addItem(client_info, client_id)
        except Exception as e:
            print(e)

    def acceptClient(self):
        client_id = self.comboBoxForChosingClients.currentData()  # отримуємо _id вибраного клієнта
        if client_id:
            delete_client(client_id)  # Виклик функції видалення з передачею _id як рядка
            self.loadClientsFromDB()  # Оновлення списку клієнтів
            self.fillComboBox()  # Оновлення comboBox
            QMessageBox.information(self, "Видалення", "Клієнт успішно видалений.")
        else:
            QMessageBox.warning(self, "Помилка", "Не вдалося визначити ID клієнта для видалення.")

    def denyClient(self):
        client_id = self.comboBoxForChosingClients.currentData()  # отримуємо _id вибраного клієнта
        if client_id:
            delete_client(client_id)  # Виклик функції видалення з передачею _id як рядка
            self.loadClientsFromDB()  # Оновлення списку клієнтів
            self.fillComboBox()  # Оновлення comboBox
            QMessageBox.information(self, "Видалення", "Клієнт успішно видалений.")
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
        except Exception as e:
            print(e)

    def loadClientsFromDB(self):
        try:
            self.comboBoxForChosingClients.clear()  # Очищення comboBox перед заповненням
            clients = get_clients()  # отримуємо список клієнтів з вашої БД
            self.tableWidgetForOutputClients.setRowCount(0)  # Очищення таблиці перед заповненням
            for client in clients:
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

        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainForm = ClientManagementForm()
    mainForm.show()
    sys.exit(app.exec_())
