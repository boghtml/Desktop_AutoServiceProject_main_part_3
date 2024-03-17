from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from Calses.AutoService import AutoService
from Calses.signals import signals
from DataBase_trial.DataBase import get_busy_employees, set_worker_free, get_busy_employees_ids
from FormDesign.EmployeeReportForm_design import Ui_Form  # Імпортуємо UI клас


class EmployeeReportForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.autoService = AutoService.get_instance()

        try:
            self.loadEmployees()
        except Exception as e:
            print(e)

        self.pushButtonForMoveWorkerToFree.clicked.connect(self.moveWorkerToFree)

        signals.employee_status_changed.connect(self.updateEmployeeData)
        signals.employee_added.connect(self.updateEmployeeData)

        self.updateEmployeeData()

    def updateEmployeeData(self):
        self.loadEmployees()

    def loadEmployees(self):
        self.tableWidgetForFreeWorker.setRowCount(0)
        self.tableWidgetForBusyWorker.setRowCount(0)
        self.comboBoxChoseWorkerForMoveToFree.clear()

        busy_employees_ids = get_busy_employees_ids()  # Отримуємо ID зайнятих працівників

        free_workers = [worker for worker in self.autoService.getEmployees() if
                        worker.get_id() not in busy_employees_ids]

        for employee in free_workers:
            rowCount = self.tableWidgetForFreeWorker.rowCount()
            self.tableWidgetForFreeWorker.insertRow(rowCount)
            self.tableWidgetForFreeWorker.setItem(rowCount, 0, QTableWidgetItem(str(employee.get_name())))
            self.tableWidgetForFreeWorker.setItem(rowCount, 1, QTableWidgetItem(str(employee.get_position())))
            self.tableWidgetForFreeWorker.setItem(rowCount, 2, QTableWidgetItem(str(employee.get_salary())))

        busy_employees = get_busy_employees()
        for employee in busy_employees:
            rowCount = self.tableWidgetForBusyWorker.rowCount()
            self.tableWidgetForBusyWorker.insertRow(rowCount)
            self.tableWidgetForBusyWorker.setItem(rowCount, 0, QTableWidgetItem(employee['name']))
            self.tableWidgetForBusyWorker.setItem(rowCount, 1, QTableWidgetItem(employee['position']))
            self.tableWidgetForBusyWorker.setItem(rowCount, 2, QTableWidgetItem(str(employee['salary'])))
            self.comboBoxChoseWorkerForMoveToFree.addItem(employee['name'], employee['_id'])

    def moveWorkerToFree(self):
        try:
            selected_index = self.comboBoxChoseWorkerForMoveToFree.currentIndex()
            selected_worker_id = self.comboBoxChoseWorkerForMoveToFree.itemData(selected_index)
            set_worker_free(selected_worker_id)  # Припускаємо, що ця функція існує
            self.loadEmployees()  # Перезавантаження списків працівників
            signals.employee_status_changed.emit()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    register_form = EmployeeReportForm()
    register_form.show()
    sys.exit(app.exec_())
