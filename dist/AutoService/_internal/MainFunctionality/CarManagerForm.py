from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from Clases.AutoService import AutoService
from Clases.Car import Car
from Clases.signals import signals
from DataBase.DataBase import add_car_base, remove_car_base, update_car_base, remove_car_base_event
from FormDesign.FormHandlers.CarManagementForm_design import Ui_CarManegerForm

from MainFunctionality.EditingForCarsForm import EditingForCarsForm


class CarManegerForm(QtWidgets.QWidget, Ui_CarManegerForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.autoService = AutoService.get_instance()

        self.initializeUI()

        self.initializeServices()

        self.pushButtonForAddCar.clicked.connect(self.addCar)
        self.pushButtonForSearching.clicked.connect(self.searchCarByBrand)
        self.pushButtonAplySort.clicked.connect(self.applySorting)
        self.pushButtonForDelatingCar.clicked.connect(self.deleteCar)
        self.tableWidgetForOutputCars.installEventFilter(self)
        self.pushButtonForEditingCar.clicked.connect(self.openEditingForm)

        signals.order_making_client.connect(self.updateTable)

    def addCar(self):
        brand = self.lineEditForMarkInput.text().strip()
        model = self.lineEditForModelInput.text().strip()
        year = self.lineEditForYearCreatInput.text().strip()

        # Перевірка, чи всі поля заповнені
        if not brand or not model or not year:
            QMessageBox.warning(self, 'Помилка', 'Будь ласка, заповніть всі поля!')
            return

        # Перевірка, чи рік випуску є числом
        if not year.isdigit():
            QMessageBox.warning(self, 'Помилка', 'Рік випуску має бути числом!')
            return

        if len(year) != 4 or not (1886 <= int(year) <= 2100):
            QMessageBox.warning(self, 'Помилка',
                                'Рік випуску має бути чотирьохзначним числом та прийнамні більше 1886!')
            return

        car = Car(brand, model, int(year))

        try:
            result = add_car_base(car)  # Припустимо, що ця функція повертає результат вставки
            car._id = result.inserted_id
        except Exception as e:
            QMessageBox.critical(self, "Помилка додавання", str(e))
            return

        self.autoService.add_carToStart(car)
        signals.car_added.emit()
        self.updateTable()

        # Очищення форм вводу після успішного додавання
        self.lineEditForMarkInput.clear()
        self.lineEditForModelInput.clear()
        self.lineEditForYearCreatInput.clear()

        self.updateDeleteComboBox()

    def searchCarByBrand(self):
        searchQuery = self.lineEditForSearchingAutoMark.text().strip().lower()
        searchResults = [car for car in self.autoService.get_cars() if searchQuery in car.brand.lower()]

        if not searchResults:
            QtWidgets.QMessageBox.information(self, "Пошук", "Автомобілі не знайдені.")
            self.updateTableSorting(searchResults)
        else:
            self.updateTableSorting(searchResults)

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
        self.updateTableSorting(sorted_cars)

    # видалення через comBoBox
    def deleteCar(self):
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

    # Видалення при натисканні Dlete
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Delete
                and source is self.tableWidgetForOutputCars):
            self.confirmDeletion()
        return super(CarManegerForm, self).eventFilter(source, event)

    def confirmDeletion(self):
        try:
            selected_items = self.tableWidgetForOutputCars.selectedItems()
            if selected_items:
                selected_row = selected_items[0].row()
                car = self.autoService.get_cars()[selected_row]  # Припустимо, кожен car має атрибут _id
                reply = QMessageBox.question(self, 'Підтвердження видалення',
                                             f"Ви впевнені, що хочете видалити автомобіль {car.brand} {car.model} року {car.year}?",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    if remove_car_base_event(car._id):  # Використання _id для видалення
                        self.autoService.remove_car(selected_row)
                        self.tableWidgetForOutputCars.removeRow(selected_row)
                        signals.car_added.emit()
                        QMessageBox.information(self, "Успіх", "Автомобіль видалено успішно.")
                    else:
                        QMessageBox.warning(self, "Помилка", "Не вдалося видалити автомобіль.")
            else:
                QMessageBox.information(self, 'Інформація', 'Будь ласка, виберіть автомобіль для видалення.')
        except Exception as e:
            print(e)

    # оновлення ініціалізація
    def initializeServices(self):
        self.updateTable()
        self.updateDeleteComboBox()

    def updateDeleteComboBox(self):
        self.comboBoxChoseCarForDelete.clear()
        for car in self.autoService.get_cars():
            car_info = f"{car.brand} {car.model} {car.year}"
            self.comboBoxChoseCarForDelete.addItem(car_info)

    def updateTable(self):
        self.tableWidgetForOutputCars.setRowCount(0)
        for car in self.autoService.get_cars():
            rowPosition = self.tableWidgetForOutputCars.rowCount()
            self.tableWidgetForOutputCars.insertRow(rowPosition)
            self.tableWidgetForOutputCars.setItem(rowPosition, 0, QTableWidgetItem(car.brand))
            self.tableWidgetForOutputCars.setItem(rowPosition, 1, QTableWidgetItem(car.model))
            self.tableWidgetForOutputCars.setItem(rowPosition, 2, QTableWidgetItem(str(car.year)))

    def updateTableSorting(self, cars):
        self.tableWidgetForOutputCars.setRowCount(0)
        for car in cars:
            rowPosition = self.tableWidgetForOutputCars.rowCount()
            self.tableWidgetForOutputCars.insertRow(rowPosition)
            self.tableWidgetForOutputCars.setItem(rowPosition, 0, QTableWidgetItem(car.brand))
            self.tableWidgetForOutputCars.setItem(rowPosition, 1, QTableWidgetItem(car.model))
            self.tableWidgetForOutputCars.setItem(rowPosition, 2, QTableWidgetItem(str(car.year)))

    # ------ робота із Формою редагування
    def openEditingForm(self):
        try:
            selected_items = self.tableWidgetForOutputCars.selectedItems()
            if selected_items:
                selected_row = selected_items[0].row()
                self.currentCar = self.autoService.get_cars()[selected_row]  # Збереження поточного автомобіля
                self.editingForm = EditingForCarsForm(self.currentCar)
                self.editingForm.show()
                self.editingForm.pushButton_ForAplyEditingAuto.clicked.connect(self.saveCarChanges)
                self.editingForm.pushButtonForDenyEditingAuto.clicked.connect(self.editingForm.close)
        except Exception as e:
            print(e)

    def saveCarChanges(self):
        try:
            updated_brand = self.editingForm.lineEditForMarkInput.text().strip()
            updated_model = self.editingForm.lineEditForModelInput.text().strip()
            updated_year_text = self.editingForm.lineEditForYearCreatInput.text().strip()

            if not updated_brand or not updated_model or not updated_year_text:
                QMessageBox.warning(self, "Помилка", "Будь ласка, заповніть всі поля.")
                return

            try:
                updated_year = int(updated_year_text)
                if updated_year < 1900 or updated_year > 2100:
                    QMessageBox.warning(self, "Помилка", "Рік випуску має бути в діапазоні від 1900 до 2100.")
                    return
            except ValueError:
                QMessageBox.warning(self, "Помилка", "Рік випуску має бути цілим числом.")
                return

            self.currentCar.brand = updated_brand
            self.currentCar.model = updated_model
            self.currentCar.year = updated_year

            self.autoService.update_car(self.currentCar)
            update_car_base(self.currentCar)
            self.editingForm.close()

            self.initializeServices()
        except Exception as e:
            print(e)

    # ініціалізація елементів та tooltip
    def initializeUI(self):
        self.comboBoxForSorting.addItem("Звичайний порядок")
        columns = ["Марка", "Модель", "Рік випуску"]
        self.comboBoxForSorting.addItems(columns)

        self.lineEditForMarkInput.setToolTip("Введіть марку автомобіля")
        self.lineEditForModelInput.setToolTip("Введіть модель автомобіля")
        self.lineEditForYearCreatInput.setToolTip("Введіть рік випуску автомобіля")
        self.pushButtonForAddCar.setToolTip("Натисніть, щоб додати новий автомобіль")
        self.tableWidgetForOutputCars.setToolTip("Таблиця зі списком автомобілів")
        self.comboBoxChoseCarForDelete.setToolTip("Виберіть автомобіль для видалення з цього списку")
        self.pushButtonForDelatingCar.setToolTip("Натисніть, щоб видалити вибраний автомобіль із comboBox")
        self.lineEditForSearchingAutoMark.setToolTip(
            "Введіть марку для пошуку автомобілів,\nщоб вивести усіх видаліть весь текст і натисніть кнопку ще раз ")
        self.comboBoxForSorting.setToolTip("Виберіть критерій сортування автомобілів")
        self.pushButtonAplySort.setToolTip("Натисніть, щоб посортувати автомобілі за вибраним критерієм")
        self.pushButtonForEditingCar.setToolTip(
            "Натисніть на рядок таблички і потім на цю кнопку\nщоб редагувати вибраний автомобіль")
        self.pushButtonForSearching.setToolTip("Натисніть, щоб виконати пошук автомобілів за введеною маркою")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainForm = CarManegerForm()
    mainForm.show()
    sys.exit(app.exec_())
