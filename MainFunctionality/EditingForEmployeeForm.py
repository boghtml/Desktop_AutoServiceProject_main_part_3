from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Clases.AutoService import AutoService
from DataBase.DataBase import update_employee_base
from FormDesign.FormHandlers.EditingForEmpoleeForm_design import Ui_Form


class EditingForEmployeeForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self, employee):
        super().__init__()
        self.setupUi(self)
        self.initializeUItooltip()

        self.autoService = AutoService.get_instance()
        self.employee = employee
        self.fillFormData()

    def fillFormData(self):
        self.lineEditForNameInput.setText(self.employee.name)
        self.lineEditForPositionInput.setText(self.employee.position)
        self.lineEditForIncomeInput.setText(str(self.employee.salary))

    def initializeUItooltip(self):
        self.labelNameInput.setToolTip("Оновіть ім'я працівника за потреби")
        self.labelIncomeIInput.setToolTip("Оновіть дохід працівника за потреби")
        self.pushButtonForDenyEditingEmpoyee.setToolTip("Натисніть, щоб скасувати редагування")
        self.pushButton_ForAplyEditingEmployee.setToolTip("Натисніть, щоб підтвердити зміни")
        self.labeForPositionInput.setToolTip("Оновіть посаду працівника за потреби")
        self.label_For_Editing_Employee.setToolTip("Введіть дані для редагування інформації про працівника")
