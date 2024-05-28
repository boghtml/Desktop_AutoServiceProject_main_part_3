from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Clases.AutoService import AutoService
from Clases.Employee import Employee
from Clases.signals import signals
from DataBase.DataBase import add_employee_base, remove_employees_base, update_employee_base
from FormDesign.FormHandlers.EmployeeManagementForm_design import Ui_Form
from MainFunctionality.EditingForEmployeeForm import EditingForEmployeeForm


class EmployeeManegementForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.autoService = AutoService.get_instance()

        self.initializeUI()

        self.initializeServices()

        self.pushButtonForAddWorker.clicked.connect(self.addWorker)
        self.pushButtonForSearching.clicked.connect(self.searchWorker)
        self.pushButtonAplySort.clicked.connect(self.sortByColumn)
        self.pushButtonForDelatingWorker.clicked.connect(self.deleteWorker)
        self.tableWidgetForOutputWorker.installEventFilter(self)

        self.pushButtonForEditingWorker.clicked.connect(self.openEditingForm)

    def openEditingForm(self):
        try:
            selected_items = self.tableWidgetForOutputWorker.selectedItems()
            if selected_items:
                selected_row = selected_items[0].row()
                employee = self.autoService.getEmployees()[selected_row]
                self.editingForm = EditingForEmployeeForm(employee)
                self.editingForm.show()
                self.editingForm.pushButton_ForAplyEditingEmployee.clicked.connect(self.saveEmployeeChanges)
                self.editingForm.pushButtonForDenyEditingEmpoyee.clicked.connect(self.editingForm.close)
        except Exception as e:
            print(e)

    def saveEmployeeChanges(self):
        try:
            updated_name = self.editingForm.lineEditForNameInput.text().strip()
            updated_position = self.editingForm.lineEditForPositionInput.text().strip()
            updated_income_text = self.editingForm.lineEditForIncomeInput.text().strip()

            print("Данні які записані:", updated_name, updated_position, updated_income_text)
            # Перевірка на пусті рядки
            if not updated_name or not updated_position or not updated_income_text:
                QMessageBox.warning(self, "Помилка", "Будь ласка, заповніть всі поля.")
                return
            try:
                updated_income = float(updated_income_text)
                if updated_income < 0:
                    QMessageBox.warning(self, 'Помилка', 'Дохід не може бути від\'ємним.')
                    return
                if updated_income > 11000 and updated_income > 0:  # Припустимо, максимальний дохід не може перевищувати 100,000
                    QMessageBox.warning(self, 'Помилка', 'Дохід занадто великий.')
                    return
            except ValueError:
                QMessageBox.warning(self, 'Помилка', 'Дохід має бути числом.')
                return

            # Оновлення об'єкта Employee
            self.editingForm.employee.name = updated_name
            self.editingForm.employee.position = updated_position
            self.editingForm.employee.salary = updated_income

            print("Данні які запишуть новий об'єкт", updated_name, updated_position, updated_income)

            self.autoService.update_employee(self.editingForm.employee)
            update_employee_base(self.editingForm.employee)

            self.updateEmployeeTable()
            self.updateDeleteComboBox()

            self.editingForm.close()
        except Exception as e:
            print(e)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Delete and source is self.tableWidgetForOutputWorker:
            self.confirmDeletionWorker()
        return super(EmployeeManegementForm, self).eventFilter(source, event)

    def confirmDeletionWorker(self):
        try:
            selected_items = self.tableWidgetForOutputWorker.selectedItems()
            if selected_items:
                selected_row = selected_items[0].row()
                selected_employee = self.autoService.getEmployees()[selected_row]

                reply = QMessageBox.question(self, 'Підтвердження видалення',
                                             "Ви впевнені, що хочете видалити обраного працівника?",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    remove_employees_base(selected_employee._id)
                    self.autoService.removeEmployee(selected_row)

                    self.initializeServices()
                    # self.updateEmployeeTable()
            else:
                QMessageBox.information(self, 'Інформація', 'Будь ласка, виберіть працівника для видалення.')
        except Exception as e:
            print(e)

    def addWorker(self):
        name = self.lineEditForNameInput.text().strip()
        position = self.lineEditForPositionInput.text().strip()
        income = self.lineEditForIncomeInput.text().strip()

        if not (name and position):
            QMessageBox.warning(self, 'Помилка', 'Введіть ім\'я та посаду!')
            return
        if not income:
            QMessageBox.warning(self, 'Помилка', 'Дохід не може бути порожнім.')
            return

        try:
            income = float(income)
            if income <= 0:
                QMessageBox.warning(self, 'Помилка', 'Дохід повинен бути більшим за нуль.')
                return
        except ValueError:
            QMessageBox.warning(self, 'Помилка', 'Дохід має бути числом.')
            return

        new_employee = Employee(name, position, income)
        try:
            result = add_employee_base(new_employee)
            new_employee._id = result.inserted_id
            # self.updateEmployeeTable()
            # self.updateDeleteComboBox()
        except Exception as e:
            QMessageBox.critical(self, "Помилка додавання", str(e))

        self.autoService.addEmployee(new_employee)
        signals.employee_added.emit()

        self.initializeServices()

        self.lineEditForNameInput.clear()
        self.lineEditForPositionInput.clear()
        self.lineEditForIncomeInput.clear()

    def searchWorker(self):
        searchQuery = self.lineEditForSearchingNameWorker.text().strip().lower()
        if not searchQuery:
            self.updateEmployeeTable()
        else:
            searchResults = [worker for worker in self.autoService.getEmployees() if
                             worker.name.lower().startswith(searchQuery)]
            if not searchResults:
                QtWidgets.QMessageBox.information(self, "Пошук", "Працівників не знайдено.")
                self.updateEmployeeTable(searchResults)
            else:
                self.updateEmployeeTable(searchResults)

    def sortByColumn(self):
        selected_column = self.comboBoxForSorting.currentText()
        if selected_column == "Ім'я":
            sorted_employees = sorted(self.autoService.getEmployees(), key=lambda emp: emp.get_name())
        elif selected_column == "Посада":
            sorted_employees = sorted(self.autoService.getEmployees(), key=lambda emp: emp.get_position())
        elif selected_column == "Дохід":
            sorted_employees = sorted(self.autoService.getEmployees(), key=lambda emp: emp.get_salary())
        else:
            sorted_employees = self.autoService.getEmployees()

        self.updateEmployeeTable(sorted_employees)

    def deleteWorker(self):
        selected_worker_index = self.comboBoxChoseWorkerForDelete.currentIndex()
        if selected_worker_index == -1:
            QMessageBox.warning(self, 'Помилка', 'Будь ласка, виберіть працівника для видалення.')
            return

        selected_employee = self.autoService.getEmployees()[selected_worker_index]

        remove_employees_base(selected_employee._id)  # видаляємо з бази даних за ID

        self.autoService.removeEmployee(selected_worker_index)  # видаляємо з AutoService

        self.initializeServices()
        # self.updateEmployeeTable()
        # self.updateDeleteComboBox()

    def updateDeleteComboBox(self):
        print("Оновлення comboBox")
        self.comboBoxChoseWorkerForDelete.clear()
        for employee in self.autoService.getEmployees():
            employee_info = f"{employee.get_name()} {employee.get_position()} {employee.get_salary()}"
            self.comboBoxChoseWorkerForDelete.addItem(employee_info)

    def updateEmployeeTable(self, employees=None):
        print("Оновлення таблички")
        if employees is None:
            employees = self.autoService.getEmployees()

        # Очищення таблиці перед заповненням
        self.tableWidgetForOutputWorker.setRowCount(0)

        self.tableWidgetForOutputWorker.setRowCount(len(employees))
        for row, emp in enumerate(employees):
            self.tableWidgetForOutputWorker.setItem(row, 0, QtWidgets.QTableWidgetItem(emp.get_name()))
            self.tableWidgetForOutputWorker.setItem(row, 1, QtWidgets.QTableWidgetItem(emp.get_position()))
            self.tableWidgetForOutputWorker.setItem(row, 2, QtWidgets.QTableWidgetItem(str(emp.get_salary())))

    def initializeServices(self):
        self.updateEmployeeTable()
        self.updateDeleteComboBox()

    def initializeUI(self):
        sorting_options = ["За замовчуванням", "Ім'я", "Посада", "Дохід"]
        self.comboBoxForSorting.addItems(sorting_options)

        self.pushButtonForAddWorker.setToolTip("Натисніть, щоб додати нового працівника")
        self.pushButtonForDelatingWorker.setToolTip("Натисніть, щоб видалити вибраного працівника із comboBox")
        self.pushButtonForSearching.setToolTip("Натисніть, щоб виконати пошук працівників за іменем")
        self.lineEditForSearchingNameWorker.setToolTip("Введіть ім'я працівника для пошуку та натисність кнопку поруч")
        self.comboBoxForSorting.setToolTip("Виберіть критерій сортування працівників")
        self.pushButtonAplySort.setToolTip("Натисніть, щоб посортувати працівників за вибраним критерієм")
        self.lineEditForNameInput.setToolTip("Введіть ім'я працівника")
        self.lineEditForPositionInput.setToolTip("Введіть посаду працівника")
        self.lineEditForIncomeInput.setToolTip("Введіть дохід працівника")
        self.tableWidgetForOutputWorker.setToolTip("Ця таблиця відображає список доступних працівників")
        self.comboBoxChoseWorkerForDelete.setToolTip("Виберіть працівника для видалення з цього списку")
        self.pushButtonForEditingWorker.setToolTip(
            "Натисніть на рядок в табличці для вибору працівника\nІ далі натисніть цю кнопку")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainForm = EmployeeManegementForm()
    mainForm.show()
    sys.exit(app.exec_())
