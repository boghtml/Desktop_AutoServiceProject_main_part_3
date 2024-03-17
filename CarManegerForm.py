from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from Calses.AutoService import AutoService
from Calses.Car import Car
from Calses.signals import signals
from DataBase_trial.DataBase import add_car_base, remove_car_base
from FormDesign.CarManegementForm_design import Ui_CarManegerForm


class CarManegerForm(QtWidgets.QWidget, Ui_CarManegerForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.autoService = AutoService.get_instance()

        self.comboBoxForSorting.addItem("Звичайний порядок")
        columns = ["Марка", "Модель", "Рік випуску"]
        self.comboBoxForSorting.addItems(columns)

        # Рбота не з інтерфейсом

        self.initializeServices()
        self.pushButtonForAddCar.clicked.connect(self.addCar)
        self.pushButtonForSearching.clicked.connect(self.searchCarByBrand)

        self.pushButtonAplySort.clicked.connect(self.applySorting)
        self.pushButtonForDelatingCar.clicked.connect(self.deleteCar1)

        self.tableWidgetForOutputCars.installEventFilter(self)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Delete
                and source is self.tableWidgetForOutputCars):
            self.confirmDeletion()
        return super(CarManegerForm, self).eventFilter(source, event)

    def confirmDeletion(self):
        selected_items = self.tableWidgetForOutputCars.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            car_brand = self.tableWidgetForOutputCars.item(selected_row, 0).text()
            car_model = self.tableWidgetForOutputCars.item(selected_row, 1).text()
            car_year = self.tableWidgetForOutputCars.item(selected_row, 2).text()
            reply = QMessageBox.question(self, 'Підтвердження видалення',
                                         f"Ви впевнені, що хочете видалити автомобіль:\n{car_brand} {car_model} {car_year} ?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.autoService.remove_car(selected_row)
                signals.car_added.emit()
                self.tableWidgetForOutputCars.removeRow(selected_row)
                self.updateDeleteComboBox()
        else:
            QMessageBox.information(self, 'Інформація', 'Будь ласка, виберіть автомобіль для видалення.')

    def applySorting(self):
        selected_column = self.comboBoxForSorting.currentText()
        if selected_column == "Марка":
            # Сортувати за маркою
            sorted_cars = sorted(self.autoService.get_cars(), key=lambda car: car.brand)
        elif selected_column == "Модель":
            # Сортувати за моделлю
            sorted_cars = sorted(self.autoService.get_cars(), key=lambda car: car.model)
        elif selected_column == "Рік випуску":
            # Сортувати за роком випуску
            sorted_cars = sorted(self.autoService.get_cars(), key=lambda car: car.year)
        elif selected_column == "Звичайний порядок":
            sorted_cars = self.autoService.get_cars()
        else:
            sorted_cars = self.autoService.get_cars()

        # Оновлення таблиці з відсортованими даними
        self.updateTable1(sorted_cars)

    def updateTable1(self, cars):
        self.tableWidgetForOutputCars.setRowCount(0)
        for car in cars:
            rowPosition = self.tableWidgetForOutputCars.rowCount()
            self.tableWidgetForOutputCars.insertRow(rowPosition)
            self.tableWidgetForOutputCars.setItem(rowPosition, 0, QTableWidgetItem(car.brand))
            self.tableWidgetForOutputCars.setItem(rowPosition, 1, QTableWidgetItem(car.model))
            self.tableWidgetForOutputCars.setItem(rowPosition, 2, QTableWidgetItem(str(car.year)))

    def addCar(self):
        brand = self.lineEditForMarkInput.text()
        model = self.lineEditForModelInput.text()
        year = self.lineEditForYearCreatInput.text()
        if not (brand and model and year.isdigit()):
            QMessageBox.warning(self, 'Помилка', 'Введіть коректні дані!')
            return

        car = Car(brand, model, int(year))

        try:
            result = add_car_base(car)  # Припустимо, що ця функція повертає результат вставки
            car._id = result.inserted_id
        # car._id = result.inserted_id
        except Exception as e:
            QMessageBox.critical(self, "Помилка додавання", str(e))

        self.autoService.add_car(car)

        signals.car_added.emit()
        
        self.updateTable()

        # Очищення форм вводу
        self.lineEditForMarkInput.clear()
        self.lineEditForModelInput.clear()
        self.lineEditForYearCreatInput.clear()

        self.updateDeleteComboBox()

    #    def updateTable(self):
    #       self.tableWidgetForOutputCars.setRowCount(0)
    #
    #       for car in get_cars():
    #          rowPosition = self.tableWidgetForOutputCars.rowCount()
    #          self.tableWidgetForOutputCars.insertRow(rowPosition)
    #           self.tableWidgetForOutputCars.setItem(rowPosition, 0, QTableWidgetItem(car['brand']))
    #            self.tableWidgetForOutputCars.setItem(rowPosition, 1, QTableWidgetItem(car['model']))
    #           self.tableWidgetForOutputCars.setItem(rowPosition, 2, QTableWidgetItem(str(car['year'])))

    def updateTable(self):
        self.tableWidgetForOutputCars.setRowCount(0)
        for car in self.autoService.get_cars():
            rowPosition = self.tableWidgetForOutputCars.rowCount()
            self.tableWidgetForOutputCars.insertRow(rowPosition)
            self.tableWidgetForOutputCars.setItem(rowPosition, 0, QTableWidgetItem(car.brand))
            self.tableWidgetForOutputCars.setItem(rowPosition, 1, QTableWidgetItem(car.model))
            self.tableWidgetForOutputCars.setItem(rowPosition, 2, QTableWidgetItem(str(car.year)))

    def initializeServices(self):
        self.updateTable()
        self.updateDeleteComboBox()

    def updateDeleteComboBox(self):
        self.comboBoxChoseCarForDelete.clear()
        for car in self.autoService.get_cars():
            car_info = f"{car.brand} {car.model} {car.year}"
            self.comboBoxChoseCarForDelete.addItem(car_info)

    def searchCarByBrand(self):
        searchQuery = self.lineEditForSearchingAutoMark.text().strip().lower()
        searchResults = [car for car in self.autoService.get_cars() if searchQuery in car.brand.lower()]

        if not searchResults:
            QtWidgets.QMessageBox.information(self, "Пошук", "Автомобілі не знайдені.")
            self.updateTable1(searchResults)
        else:
            self.updateTable1(searchResults)

    def deleteCar1(self):
        selected_car_index = self.comboBoxChoseCarForDelete.currentIndex()
        if selected_car_index == -1:
            QMessageBox.warning(self, 'Помилка', 'Будь ласка, виберіть автомобіль для видалення.')
            return

        reply = QMessageBox.question(self, 'Підтвердження видалення',
                                     'Ви впевнені, що хочете видалити вибраний автомобіль?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            car_to_remove = self.autoService.get_cars()[selected_car_index]
            try:
                print(car_to_remove)
                remove_car_base(car_to_remove._id)  # Видаляємо за _id
            except Exception as e:
                print(e)
            # Видалення з локального списку та оновлення UI
            self.autoService.remove_car(selected_car_index)
            signals.car_added.emit()
            self.updateTable()
            self.updateDeleteComboBox()

    def deleteCar(self):
        # Перевіряємо, чи індекс вибраного елемента в comboBoxChoseCarForDelete не дорівнює -1 (що означає відсутність вибору)
        selected_car_index = self.comboBoxChoseCarForDelete.currentIndex()
        if selected_car_index == -1:
            QMessageBox.warning(self, 'Помилка', 'Будь ласка, виберіть автомобіль для видалення.')
            return

        # Діалогове вікно для підтвердження видалення
        reply = QMessageBox.question(self, 'Підтвердження видалення',
                                     'Ви впевнені, що хочете видалити вибраний автомобіль?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            car_to_remove = self.autoService.get_cars()[selected_car_index]

            # Видалення автомобіля зі списку у AutoService
            self.autoService.remove_car(selected_car_index)

            # Оновлення таблиці та комбо-бокса
            self.updateTable()
            self.updateDeleteComboBox()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainForm = CarManegerForm()
    mainForm.show()
    sys.exit(app.exec_())
