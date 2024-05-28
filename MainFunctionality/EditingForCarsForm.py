from PyQt5 import QtCore, QtWidgets

from FormDesign.FormHandlers.EditingForCarsForm_design import Ui_Form


class EditingForCarsForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self, car):
        super().__init__()
        self.setupUi(self)
        self.initializeUItooltip()

        self.car = car
        self.fillFormData()

    def fillFormData(self):
        self.lineEditForMarkInput.setText(self.car.brand)
        self.lineEditForModelInput.setText(self.car.model)
        self.lineEditForYearCreatInput.setText(str(self.car.year))

    def initializeUItooltip(self):
        self.label_For_Editing_auto.setToolTip("Введіть дані для редагування інформації про авто")
        self.labelMarkIput.setToolTip("Оновіть марку авто, за потреби")
        self.labeForModelIput.setToolTip("Оновіть модель авто, за потреби")
        self.labelYearInput.setToolTip("Оновіть рік випуску авто, за потреби")
        self.pushButtonForDenyEditingAuto.setToolTip("Натисніть, щоб скасувати редагування")
        self.pushButton_ForAplyEditingAuto.setToolTip("Натисніть, щоб підтвердити зміни")
