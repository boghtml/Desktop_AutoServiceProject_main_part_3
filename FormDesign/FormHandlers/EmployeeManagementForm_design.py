# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmployeeManegementForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(952, 569)
        self.pushButtonForAddWorker = QtWidgets.QPushButton(Form)
        self.pushButtonForAddWorker.setGeometry(QtCore.QRect(690, 190, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButtonForAddWorker.setFont(font)
        self.pushButtonForAddWorker.setStyleSheet("QPushButton {\n"
                                                  "    background-color: #4CAF50; /* Зелений колір */\n"
                                                  "    border: none;\n"
                                                  "    color: white;\n"
                                                  "    padding: 10px 20px;\n"
                                                  "    text-align: center;\n"
                                                  "    text-decoration: none;\n"
                                                  "    display: inline-block;\n"
                                                  "    font-size: 16px;\n"
                                                  "border:1px solid black; /* Чорний бордер */\n"
                                                  "    margin: 4px 2px;\n"
                                                  "    cursor: pointer;\n"
                                                  "    border-radius: 5px; /* Округлені кути */\n"
                                                  "}\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: #45a049; /* Зелений колір при наведенні */\n"
                                                  "}\n"
                                                  "")
        self.pushButtonForAddWorker.setObjectName("pushButtonForAddWorker")
        self.pushButtonForDelatingWorker = QtWidgets.QPushButton(Form)
        self.pushButtonForDelatingWorker.setGeometry(QtCore.QRect(680, 320, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButtonForDelatingWorker.setFont(font)
        self.pushButtonForDelatingWorker.setStyleSheet("QPushButton {\n"
                                                       "    background-color: #f44336; /* Червоний колір */\n"
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
                                                       "    background-color: #d32f2f; /* Червоний колір при наведенні */\n"
                                                       "}\n"
                                                       "")
        self.pushButtonForDelatingWorker.setObjectName("pushButtonForDelatingWorker")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(40, 50, 901, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButtonForSearching = QtWidgets.QPushButton(self.frame)
        self.pushButtonForSearching.setGeometry(QtCore.QRect(200, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButtonForSearching.setFont(font)
        self.pushButtonForSearching.setStyleSheet("QPushButton {\n"
                                                  "    background-color: #FFEB3B; /* Жовтий колір */\n"
                                                  "    border: none;\n"
                                                  "    color: black; /* Чорний колір тексту для кращої видимості */\n"
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
                                                  "    background-color: #FDD835; /* Жовтий колір при наведенні */\n"
                                                  "}\n"
                                                  "")
        self.pushButtonForSearching.setObjectName("pushButtonForSearching")
        self.lineEditForSearchingNameWorker = QtWidgets.QLineEdit(self.frame)
        self.lineEditForSearchingNameWorker.setGeometry(QtCore.QRect(20, 20, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditForSearchingNameWorker.setFont(font)
        self.lineEditForSearchingNameWorker.setObjectName("lineEditForSearchingNameWorker")
        self.comboBoxForSorting = QtWidgets.QComboBox(self.frame)
        self.comboBoxForSorting.setGeometry(QtCore.QRect(390, 20, 181, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxForSorting.setFont(font)
        self.comboBoxForSorting.setObjectName("comboBoxForSorting")
        self.pushButtonAplySort = QtWidgets.QPushButton(self.frame)
        self.pushButtonAplySort.setGeometry(QtCore.QRect(580, 10, 141, 51))
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
                                              "border:1px solid black; /* Чорний бордер */\n"
                                              "    margin: 4px 2px;\n"
                                              "    cursor: pointer;\n"
                                              "    border-radius: 5px; /* Округлені кути */\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: #757575; /* Сірий колір при наведенні */\n"
                                              "}\n"
                                              "")
        self.pushButtonAplySort.setObjectName("pushButtonAplySort")
        self.labelIncomeIInput = QtWidgets.QLabel(self.frame)
        self.labelIncomeIInput.setGeometry(QtCore.QRect(450, 70, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelIncomeIInput.setFont(font)
        self.labelIncomeIInput.setObjectName("labelIncomeIInput")
        self.lineEditForPositionInput = QtWidgets.QLineEdit(self.frame)
        self.lineEditForPositionInput.setGeometry(QtCore.QRect(290, 70, 135, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditForPositionInput.setFont(font)
        self.lineEditForPositionInput.setObjectName("lineEditForPositionInput")
        self.labeForPositionIput = QtWidgets.QLabel(self.frame)
        self.labeForPositionIput.setGeometry(QtCore.QRect(216, 70, 64, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labeForPositionIput.setFont(font)
        self.labeForPositionIput.setObjectName("labeForPositionIput")
        self.lineEditForNameInput = QtWidgets.QLineEdit(self.frame)
        self.lineEditForNameInput.setGeometry(QtCore.QRect(60, 70, 135, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditForNameInput.setFont(font)
        self.lineEditForNameInput.setObjectName("lineEditForNameInput")
        self.labelNameInput = QtWidgets.QLabel(self.frame)
        self.labelNameInput.setGeometry(QtCore.QRect(15, 70, 39, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelNameInput.setFont(font)
        self.labelNameInput.setObjectName("labelNameInput")
        self.lineEditForIncomeInput = QtWidgets.QLineEdit(self.frame)
        self.lineEditForIncomeInput.setGeometry(QtCore.QRect(512, 70, 135, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditForIncomeInput.setFont(font)
        self.lineEditForIncomeInput.setObjectName("lineEditForIncomeInput")
        self.label_main_worker = QtWidgets.QLabel(Form)
        self.label_main_worker.setGeometry(QtCore.QRect(340, 0, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_main_worker.setFont(font)
        self.label_main_worker.setObjectName("label_main_worker")
        self.tableWidgetForOutputWorker = QtWidgets.QTableWidget(Form)
        self.tableWidgetForOutputWorker.setGeometry(QtCore.QRect(40, 160, 591, 391))
        self.tableWidgetForOutputWorker.setObjectName("tableWidgetForOutputWorker")
        self.tableWidgetForOutputWorker.setColumnCount(3)
        self.tableWidgetForOutputWorker.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForOutputWorker.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForOutputWorker.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForOutputWorker.setHorizontalHeaderItem(2, item)
        self.labelWorkerDelateChoice = QtWidgets.QLabel(Form)
        self.labelWorkerDelateChoice.setGeometry(QtCore.QRect(661, 251, 280, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelWorkerDelateChoice.setFont(font)
        self.labelWorkerDelateChoice.setObjectName("labelWorkerDelateChoice")
        self.comboBoxChoseWorkerForDelete = QtWidgets.QComboBox(Form)
        self.comboBoxChoseWorkerForDelete.setGeometry(QtCore.QRect(680, 280, 211, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxChoseWorkerForDelete.setFont(font)
        self.comboBoxChoseWorkerForDelete.setObjectName("comboBoxChoseWorkerForDelete")
        self.pushButtonForEditingWorker = QtWidgets.QPushButton(Form)
        self.pushButtonForEditingWorker.setGeometry(QtCore.QRect(690, 380, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButtonForEditingWorker.setFont(font)
        self.pushButtonForEditingWorker.setStyleSheet("QPushButton {\n"
                                                      "    background-color: #2196F3; /* Синій колір */\n"
                                                      "    border: none;\n"
                                                      "    color: white;\n"
                                                      "    padding: 10px 20px;\n"
                                                      "    text-align: center;\n"
                                                      "    text-decoration: none;\n"
                                                      "    display: inline-block;\n"
                                                      "    font-size: 16px;\n"
                                                      "border:1px solid black; /* Чорний бордер */\n"
                                                      "    margin: 4px 2px;\n"
                                                      "    cursor: pointer;\n"
                                                      "    border-radius: 5px; /* Округлені кути */\n"
                                                      "}\n"
                                                      "QPushButton:hover {\n"
                                                      "    background-color: #1976D2; /* Синій колір при наведенні */\n"
                                                      "}\n"
                                                      "")
        self.pushButtonForEditingWorker.setObjectName("pushButtonForEditingWorker")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "EmployeeManegementForm"))
        self.pushButtonForAddWorker.setText(_translate("Form", "Додати працівника"))
        self.pushButtonForDelatingWorker.setText(_translate("Form", "Видалити працівника"))
        self.pushButtonForSearching.setText(_translate("Form", "Здійснити пошук"))
        self.pushButtonAplySort.setText(_translate("Form", "Посортувати"))
        self.labelIncomeIInput.setText(_translate("Form", "Дохід:"))
        self.labeForPositionIput.setText(_translate("Form", "Посада:"))
        self.labelNameInput.setText(_translate("Form", "Ім\'я:"))
        self.label_main_worker.setText(_translate("Form", "Працівники"))
        item = self.tableWidgetForOutputWorker.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ім\'я"))
        item = self.tableWidgetForOutputWorker.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Посада"))
        item = self.tableWidgetForOutputWorker.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Дохід"))
        self.labelWorkerDelateChoice.setText(_translate("Form", "Оберіть працівника для видалення:"))
        self.pushButtonForEditingWorker.setText(_translate("Form", "Змінити"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
