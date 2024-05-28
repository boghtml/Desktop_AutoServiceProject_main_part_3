# Файл: StatusChangeForm.py
from PyQt5 import QtWidgets

from DataBase.DataBase import update_client_status
from FormDesign.FormHandlers.ChangingStatusForClientsForm_design import Ui_Form


class StatusChangeForm(QtWidgets.QDialog, Ui_Form):
    def __init__(self, client, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initializeUItooltip()

        self.client = client
        self.fillFormData()

        self.pushButton_ForAplyEditingStatus.clicked.connect(self.accept)

    def fillFormData(self):
        if self.client is None:
            QtWidgets.QMessageBox.warning(self, "Помилка", "Клієнта не знайдено.")
            self.reject()  # Закриваємо форму, якщо клієнт не знайдений
            return

        try:
            self.lineEdit_ForNamePrint.setText(self.client['name'])
            self.lineEdit_ForNamePrint.setReadOnly(True)
            self.lineEdi_ForPositionPrint.setText(self.client['surname'])
            self.lineEdi_ForPositionPrint.setReadOnly(True)
            self.lineEdit_ForTelephonePrint.setText(self.client['phone'])
            self.lineEdit_ForTelephonePrint.setReadOnly(True)
            self.lineEdit_ForDataPrint.setText(self.client['date'])
            self.lineEdit_ForDataPrint.setReadOnly(True)
            self.comboBox_ForChanging.setCurrentText(self.client.get('status', 'Очікується'))
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self, "Помилка", "Помилка при заповненні даних.")

    def accept(self):
        # Отримання нового статусу клієнта з поля введення
        new_status = self.comboBox_ForChanging.currentText()

        # Оновлення статусу клієнта в базі даних
        try:
            update_client_status(self.client['_id'], new_status)
            super().accept()
        except Exception as e:
            # Обробка помилок при оновленні статусу
            print(f"Error updating client status: {e}")
            QtWidgets.QMessageBox.warning(self, "Помилка", "Не вдалося оновити статус клієнта.")

    def initializeUItooltip(self):
        self.label_For_Editing_Employee.setToolTip("Форма для зміни статусу замовлення клієнта")
        self.pushButton_ForDenyEditingStatus.setToolTip("Натисніть, щоб скасувати зміни")
        self.pushButton_ForAplyEditingStatus.setToolTip("Натисніть, щоб підтвердити зміни статусу замовлення")
        self.label_ForChangingStatus.setToolTip("Виберіть новий статус замовлення зі списку")
        self.comboBox_ForChanging.setToolTip(
            "Виберіть статус замовлення: Очікується, Підтверджено, Виконується, або Завершено")
