# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServiceManagementForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Calses.AutoService import AutoService
from Calses.Service import Service
from Calses.signals import signals
from DataBase_trial.DataBase import add_service_base, remove_service_base
from FormDesign.ServiceManagementForm_design import Ui_Form


class ServiceManagementForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.autoService = AutoService.get_instance()

        self.tableWidgetForOutputService.setColumnWidth(0, 250)
        self.tableWidgetForOutputService.setColumnWidth(1, 100)
        # -----
        self.pushButtonForAddService.clicked.connect(self.addService)
        self.pushButtonForSearching.clicked.connect(self.searchServiceByName)

        self.comboBoxForSorting.addItem("Звичайний порядок")
        self.comboBoxForSorting.addItems(["Назва", "Ціна"])
        self.pushButtonAplySort.clicked.connect(self.applySorting)

        self.tableWidgetForOutputService.installEventFilter(self)

        self.pushButtonForDelatingService.clicked.connect(self.deleteService)

        self.initializeServices()

    def deleteService(self):
        if self.comboBoxForChoseServiceDelete.currentIndex() == -1:
            QMessageBox.warning(self, 'Помилка', 'Будь ласка, виберіть послугу для видалення.')
        else:
            selected_service_index = self.comboBoxForChoseServiceDelete.currentIndex()
            reply = QMessageBox.question(self, 'Підтвердження видалення', 'Ви впевнені?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                service_to_remove = self.autoService.get_services()[selected_service_index]
                remove_service_base(service_to_remove._id)

                self.autoService.remove_service(
                    selected_service_index)  # Припускаючи, що ви додали метод remove_service
                signals.services_added.emit()
                self.updateServiceTable()
                self.updateServiceComboBox()

                self.comboBoxForChoseServiceDelete.removeItem(
                    selected_service_index)  # Оновлення comboBoxForChoseServiceDelete

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Delete and source is self.tableWidgetForOutputService:
            self.confirmDeletionService()
        return super(ServiceManagementForm, self).eventFilter(source, event)

    def confirmDeletionService(self):
        selected_items = self.tableWidgetForOutputService.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            service_name = self.tableWidgetForOutputService.item(selected_row, 0).text()
            service_price = self.tableWidgetForOutputService.item(selected_row, 1).text()

            reply = QMessageBox.question(self, 'Підтвердження видалення',
                                         f"Ви впевнені, що хочете видалити послугу:\n{service_name} - {service_price} ?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.autoService.remove_service(selected_row)  # Припускаючи, що ви додали метод remove_service
                self.updateServiceTable()

    def applySorting(self):
        selected_sorting = self.comboBoxForSorting.currentText()
        if selected_sorting == "Назва":
            sorted_services = sorted(self.autoService.get_services(), key=lambda service: service.get_name())
        elif selected_sorting == "Ціна":
            sorted_services = sorted(self.autoService.get_services(), key=lambda service: service.get_price())
        else:
            sorted_services = self.autoService.get_services()
        self.updateServiceTable(sorted_services)

    def searchServiceByName(self):
        searchQuery = self.lineEditForSearchingServiceName.text().strip().lower()
        if not searchQuery:
            self.updateServiceTable()
        else:
            searchResults = [service for service in self.autoService.get_services() if
                             searchQuery in service.get_name().lower()]
            if not searchResults:
                QtWidgets.QMessageBox.information(self, "Пошук", "Послуг не знайдено.")
                self.updateServiceTable(searchResults)
            else:
                self.updateServiceTable(searchResults)

    def addService(self):
        service_name = self.lineEditForServiceInput.text()
        price_text = self.lineEditForPriceInput.text()

        if service_name and price_text:
            try:
                price = float(price_text)
                new_service = Service(service_name, price)

                try:
                    service_id = add_service_base(new_service)  # додавання до бази даних
                    print(service_id)
                    new_service._id = service_id.inserted_id  # збереження id послуги
                    print(new_service)
                except Exception as e:
                    print(e)

                self.autoService.add_service(new_service)
                signals.services_added.emit()
                self.updateServiceTable()
                self.updateServiceComboBox()

                self.lineEditForServiceInput.clear()
                self.lineEditForPriceInput.clear()
            except ValueError:
                # Обробка помилки неправильного формату ціни
                QtWidgets.QMessageBox.warning(self, "Помилка", "Ціна має бути числовим значенням.")
        else:
            QtWidgets.QMessageBox.warning(self, "Помилка", "Будь ласка, введіть назву та ціну послуги.")

    def updateServiceTable(self, services=None):
        # Якщо список послуг не передано, використовувати усі послуги
        if services is None:
            services = self.autoService.get_services()

        self.tableWidgetForOutputService.setRowCount(0)
        row = 0
        for service in services:
            self.tableWidgetForOutputService.insertRow(row)
            self.tableWidgetForOutputService.setItem(row, 0, QtWidgets.QTableWidgetItem(service.get_name()))
            self.tableWidgetForOutputService.setItem(row, 1, QtWidgets.QTableWidgetItem(str(service.get_price())))
            row += 1

    def initializeServices(self):
        self.updateServiceTable()
        self.updateServiceComboBox()

    def updateServiceComboBox(self):
        self.comboBoxForChoseServiceDelete.clear()
        for service in self.autoService.get_services():
            self.comboBoxForChoseServiceDelete.addItem(f"{service.get_name()} - {service.get_price()}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainForm = ServiceManagementForm()
    mainForm.show()
    sys.exit(app.exec_())