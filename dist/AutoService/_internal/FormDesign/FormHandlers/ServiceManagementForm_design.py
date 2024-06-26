# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServiceManagementForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(959, 573)
        self.label_main_worker = QtWidgets.QLabel(Form)
        self.label_main_worker.setGeometry(QtCore.QRect(300, 10, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_main_worker.setFont(font)
        self.label_main_worker.setObjectName("label_main_worker")
        self.pushButtonForAddService = QtWidgets.QPushButton(Form)
        self.pushButtonForAddService.setGeometry(QtCore.QRect(680, 220, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButtonForAddService.setFont(font)
        self.pushButtonForAddService.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50; /* Зелений колір */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"border:1px solid black; /* Чорний бордер */\n"
"    cursor: pointer;\n"
"    border-radius: 5px; /* Округлені кути */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Зелений колір при наведенні */\n"
"}\n"
"")
        self.pushButtonForAddService.setObjectName("pushButtonForAddService")
        self.tableWidgetForOutputService = QtWidgets.QTableWidget(Form)
        self.tableWidgetForOutputService.setGeometry(QtCore.QRect(50, 180, 541, 351))
        self.tableWidgetForOutputService.setObjectName("tableWidgetForOutputService")
        self.tableWidgetForOutputService.setColumnCount(2)
        self.tableWidgetForOutputService.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForOutputService.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForOutputService.setHorizontalHeaderItem(1, item)
        self.comboBoxForSorting = QtWidgets.QComboBox(Form)
        self.comboBoxForSorting.setGeometry(QtCore.QRect(440, 90, 211, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxForSorting.setFont(font)
        self.comboBoxForSorting.setObjectName("comboBoxForSorting")
        self.pushButtonForSearching = QtWidgets.QPushButton(Form)
        self.pushButtonForSearching.setGeometry(QtCore.QRect(230, 80, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButtonForSearching.setFont(font)
        self.pushButtonForSearching.setStyleSheet("QPushButton {\n"
"    background-color: #FFEB3B; /* Жовтий колір */\n"
"    border: none;\n"
"    color: black; /* Чорний колір тексту для кращої видимості */\n"
"    border:1px solid black; /* Чорний бордер */\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"    border-radius: 5px; /* Округлені кути */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FDD835; /* Жовтий колір при наведенні */\n"
"}\n"
"")
        self.pushButtonForSearching.setObjectName("pushButtonForSearching")
        self.lineEditForSearchingServiceName = QtWidgets.QLineEdit(Form)
        self.lineEditForSearchingServiceName.setGeometry(QtCore.QRect(50, 90, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditForSearchingServiceName.setFont(font)
        self.lineEditForSearchingServiceName.setObjectName("lineEditForSearchingServiceName")
        self.pushButtonAplySort = QtWidgets.QPushButton(Form)
        self.pushButtonAplySort.setGeometry(QtCore.QRect(660, 70, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButtonAplySort.setFont(font)
        self.pushButtonAplySort.setStyleSheet("QPushButton {\n"
"    background-color: #9E9E9E; /* Сірий колір */\n"
"    border: none;\n"
"    color: white; /* Білий колір тексту для кращої видимості */\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"border:1px solid black; /* Чорний бордер */\n"
"    cursor: pointer;\n"
"    border-radius: 5px; /* Округлені кути */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #757575; /* Сірий колір при наведенні */\n"
"}\n"
"")
        self.pushButtonAplySort.setObjectName("pushButtonAplySort")
        self.pushButtonForDelatingService = QtWidgets.QPushButton(Form)
        self.pushButtonForDelatingService.setGeometry(QtCore.QRect(670, 360, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButtonForDelatingService.setFont(font)
        self.pushButtonForDelatingService.setStyleSheet("QPushButton {\n"
"    background-color: #f44336; /* Червоний колір */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"border:1px solid black; /* Чорний бордер */\n"
"    border-radius: 5px; /* Округлені кути */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #d32f2f; /* Червоний колір при наведенні */\n"
"}\n"
"")
        self.pushButtonForDelatingService.setObjectName("pushButtonForDelatingService")
        self.labelCarDelateChoice = QtWidgets.QLabel(Form)
        self.labelCarDelateChoice.setGeometry(QtCore.QRect(640, 280, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCarDelateChoice.setFont(font)
        self.labelCarDelateChoice.setObjectName("labelCarDelateChoice")
        self.comboBoxForChoseServiceDelete = QtWidgets.QComboBox(Form)
        self.comboBoxForChoseServiceDelete.setGeometry(QtCore.QRect(610, 320, 301, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxForChoseServiceDelete.setFont(font)
        self.comboBoxForChoseServiceDelete.setObjectName("comboBoxForChoseServiceDelete")
        self.lineEditForServiceInput = QtWidgets.QLineEdit(Form)
        self.lineEditForServiceInput.setGeometry(QtCore.QRect(197, 140, 171, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditForServiceInput.setFont(font)
        self.lineEditForServiceInput.setObjectName("lineEditForServiceInput")
        self.labelNameService = QtWidgets.QLabel(Form)
        self.labelNameService.setGeometry(QtCore.QRect(51, 140, 139, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNameService.setFont(font)
        self.labelNameService.setObjectName("labelNameService")
        self.labeForPriceIput = QtWidgets.QLabel(Form)
        self.labeForPriceIput.setGeometry(QtCore.QRect(375, 140, 118, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labeForPriceIput.setFont(font)
        self.labeForPriceIput.setObjectName("labeForPriceIput")
        self.lineEditForPriceInput = QtWidgets.QLineEdit(Form)
        self.lineEditForPriceInput.setGeometry(QtCore.QRect(500, 140, 171, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditForPriceInput.setFont(font)
        self.lineEditForPriceInput.setObjectName("lineEditForPriceInput")
        self.pushButtonForEditingService = QtWidgets.QPushButton(Form)
        self.pushButtonForEditingService.setGeometry(QtCore.QRect(680, 420, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButtonForEditingService.setFont(font)
        self.pushButtonForEditingService.setStyleSheet("QPushButton {\n"
"    background-color: #2196F3; /* Синій колір */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"border:1px solid black; /* Чорний бордер */\n"
"    cursor: pointer;\n"
"    border-radius: 5px; /* Округлені кути */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #1976D2; /* Синій колір при наведенні */\n"
"}\n"
"")
        self.pushButtonForEditingService.setObjectName("pushButtonForEditingService")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ServiceManagementForm"))
        self.label_main_worker.setText(_translate("Form", "Додавання послуг"))
        self.pushButtonForAddService.setText(_translate("Form", "Додати послугу"))
        item = self.tableWidgetForOutputService.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Назва"))
        item = self.tableWidgetForOutputService.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Ціна"))
        self.pushButtonForSearching.setText(_translate("Form", "Здійснити пошук"))
        self.pushButtonAplySort.setText(_translate("Form", "Посортувати"))
        self.pushButtonForDelatingService.setText(_translate("Form", "Видалити послгу"))
        self.labelCarDelateChoice.setText(_translate("Form", "Оберіть послугу для видалення:"))
        self.labelNameService.setText(_translate("Form", "Назва послуги:"))
        self.labeForPriceIput.setText(_translate("Form", "Введіть ціну:"))
        self.pushButtonForEditingService.setText(_translate("Form", "Змінити"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
