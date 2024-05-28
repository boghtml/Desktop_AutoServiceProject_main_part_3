from PyQt5 import QtWidgets

from Clases.AutoService import AutoService
from FormDesign.FormHandlers.EditingForServicesForm_design import Ui_Form


class EditingForServiceForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self, service):
        super().__init__()
        self.setupUi(self)
        self.initializeUItooltip()

        self.autoService = AutoService.get_instance()
        self.service = service
        self.fillFormData()

    def fillFormData(self):
        self.lineEditForServiceEditingInput.setText(self.service.name)
        self.lineEditForPriceEditingInput.setText(str(self.service.price))

    def initializeUItooltip(self):
        self.labelServiceIput.setToolTip("Оновіть назву послуги за потреби")
        self.pushButtonForDenyEditingService.setToolTip("Натисніть, щоб скасувати редагування")
        self.pushButton_ForAplyEditingService.setToolTip("Натисніть, щоб підтвердити зміни")
        self.labeForPricelIput.setToolTip("Оновіть ціну послуги за потреби")
        self.label_For_Editing_Services.setToolTip("Введіть дані для редагування інформації про послугу")
