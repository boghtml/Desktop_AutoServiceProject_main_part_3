# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangingStatusForClientsForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(552, 384)
        self.label_TelephonePrint = QtWidgets.QLabel(Form)
        self.label_TelephonePrint.setGeometry(QtCore.QRect(130, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_TelephonePrint.setFont(font)
        self.label_TelephonePrint.setObjectName("label_TelephonePrint")
        self.lineEdit_ForTelephonePrint = QtWidgets.QLineEdit(Form)
        self.lineEdit_ForTelephonePrint.setGeometry(QtCore.QRect(240, 160, 171, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_ForTelephonePrint.setFont(font)
        self.lineEdit_ForTelephonePrint.setObjectName("lineEdit_ForTelephonePrint")
        self.lineEdi_ForPositionPrint = QtWidgets.QLineEdit(Form)
        self.lineEdi_ForPositionPrint.setGeometry(QtCore.QRect(240, 120, 171, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdi_ForPositionPrint.setFont(font)
        self.lineEdi_ForPositionPrint.setObjectName("lineEdi_ForPositionPrint")
        self.labe_ForPositionPrint = QtWidgets.QLabel(Form)
        self.labe_ForPositionPrint.setGeometry(QtCore.QRect(120, 120, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labe_ForPositionPrint.setFont(font)
        self.labe_ForPositionPrint.setObjectName("labe_ForPositionPrint")
        self.label_For_Editing_Employee = QtWidgets.QLabel(Form)
        self.label_For_Editing_Employee.setGeometry(QtCore.QRect(60, 10, 441, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_For_Editing_Employee.setFont(font)
        self.label_For_Editing_Employee.setObjectName("label_For_Editing_Employee")
        self.pushButton_ForDenyEditingStatus = QtWidgets.QPushButton(Form)
        self.pushButton_ForDenyEditingStatus.setGeometry(QtCore.QRect(280, 310, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ForDenyEditingStatus.setFont(font)
        self.pushButton_ForDenyEditingStatus.setStyleSheet("QPushButton {\n"
"    background-color: #8B0000; /* Темно-червоний колір */\n"
"    color: white; /* Колір тексту */\n"
"    border-radius: 5px; /* Закруглені кути, можна налаштувати за потреби */\n"
"    padding: 5px; /* Відступ всередині кнопки */\n"
"    border: none; /* Без рамки */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FF6347; /* Світло-червоний колір */\n"
"}\n"
"")
        self.pushButton_ForDenyEditingStatus.setObjectName("pushButton_ForDenyEditingStatus")
        self.lineEdit_ForNamePrint = QtWidgets.QLineEdit(Form)
        self.lineEdit_ForNamePrint.setGeometry(QtCore.QRect(234, 74, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_ForNamePrint.setFont(font)
        self.lineEdit_ForNamePrint.setObjectName("lineEdit_ForNamePrint")
        self.pushButton_ForAplyEditingStatus = QtWidgets.QPushButton(Form)
        self.pushButton_ForAplyEditingStatus.setGeometry(QtCore.QRect(100, 310, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ForAplyEditingStatus.setFont(font)
        self.pushButton_ForAplyEditingStatus.setStyleSheet("QPushButton {\n"
"    background-color: #006400; /* Dark green color */\n"
"    color: white; /* Text color */\n"
"    border-radius: 5px; /* Rounded corners, adjust as needed */\n"
"    padding: 5px; /* Padding inside the button */\n"
"    border: none; /* No border */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #65B969; /* Light green color */\n"
"}\n"
"")
        self.pushButton_ForAplyEditingStatus.setObjectName("pushButton_ForAplyEditingStatus")
        self.label_NamePrint = QtWidgets.QLabel(Form)
        self.label_NamePrint.setGeometry(QtCore.QRect(180, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_NamePrint.setFont(font)
        self.label_NamePrint.setObjectName("label_NamePrint")
        self.label_DataMeatingPrint = QtWidgets.QLabel(Form)
        self.label_DataMeatingPrint.setGeometry(QtCore.QRect(30, 200, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_DataMeatingPrint.setFont(font)
        self.label_DataMeatingPrint.setObjectName("label_DataMeatingPrint")
        self.lineEdit_ForDataPrint = QtWidgets.QLineEdit(Form)
        self.lineEdit_ForDataPrint.setGeometry(QtCore.QRect(240, 200, 171, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_ForDataPrint.setFont(font)
        self.lineEdit_ForDataPrint.setObjectName("lineEdit_ForDataPrint")
        self.label_ForChangingStatus = QtWidgets.QLabel(Form)
        self.label_ForChangingStatus.setGeometry(QtCore.QRect(150, 250, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_ForChangingStatus.setFont(font)
        self.label_ForChangingStatus.setObjectName("label_ForChangingStatus")
        self.comboBox_ForChanging = QtWidgets.QComboBox(Form)
        self.comboBox_ForChanging.setGeometry(QtCore.QRect(240, 251, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_ForChanging.setFont(font)
        self.comboBox_ForChanging.setObjectName("comboBox_ForChanging")
        self.comboBox_ForChanging.addItem("")
        self.comboBox_ForChanging.addItem("")
        self.comboBox_ForChanging.addItem("")
        self.comboBox_ForChanging.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ChangingStatusFormClient"))
        self.label_TelephonePrint.setText(_translate("Form", "Телефон:"))
        self.labe_ForPositionPrint.setText(_translate("Form", "Прізвище:"))
        self.label_For_Editing_Employee.setText(_translate("Form", "Зміна статуса замовлення"))
        self.pushButton_ForDenyEditingStatus.setText(_translate("Form", "Скасувати"))
        self.pushButton_ForAplyEditingStatus.setText(_translate("Form", "Підтвердити"))
        self.label_NamePrint.setText(_translate("Form", "Ім\'я:"))
        self.label_DataMeatingPrint.setText(_translate("Form", "Запланована дата:"))
        self.label_ForChangingStatus.setText(_translate("Form", "Статус:"))
        self.comboBox_ForChanging.setItemText(0, _translate("Form", "Очікується"))
        self.comboBox_ForChanging.setItemText(1, _translate("Form", "Підтверджено"))
        self.comboBox_ForChanging.setItemText(2, _translate("Form", "Виконується"))
        self.comboBox_ForChanging.setItemText(3, _translate("Form", "Завершено"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())