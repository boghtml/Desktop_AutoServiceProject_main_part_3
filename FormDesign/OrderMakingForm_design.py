# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OrderMakingForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1333, 599)
        self.pushButtonForAddOrder = QtWidgets.QPushButton(Form)
        self.pushButtonForAddOrder.setGeometry(QtCore.QRect(700, 530, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonForAddOrder.setFont(font)
        self.pushButtonForAddOrder.setObjectName("pushButtonForAddOrder")
        self.label_main_auto = QtWidgets.QLabel(Form)
        self.label_main_auto.setGeometry(QtCore.QRect(300, 0, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_main_auto.setFont(font)
        self.label_main_auto.setObjectName("label_main_auto")
        self.tableWidgetForOutputCars = QtWidgets.QTableWidget(Form)
        self.tableWidgetForOutputCars.setGeometry(QtCore.QRect(20, 120, 612, 390))
        self.tableWidgetForOutputCars.setObjectName("tableWidgetForOutputCars")
        self.tableWidgetForOutputCars.setColumnCount(4)
        self.tableWidgetForOutputCars.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForOutputCars.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForOutputCars.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForOutputCars.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForOutputCars.setHorizontalHeaderItem(3, item)
        self.labeForPriceCalculate = QtWidgets.QLabel(Form)
        self.labeForPriceCalculate.setGeometry(QtCore.QRect(641, 381, 48, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labeForPriceCalculate.setFont(font)
        self.labeForPriceCalculate.setObjectName("labeForPriceCalculate")
        self.lineEditForPricePrint = QtWidgets.QLineEdit(Form)
        self.lineEditForPricePrint.setGeometry(QtCore.QRect(712, 381, 188, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditForPricePrint.setFont(font)
        self.lineEditForPricePrint.setObjectName("lineEditForPricePrint")
        self.labelDateInput = QtWidgets.QLabel(Form)
        self.labelDateInput.setGeometry(QtCore.QRect(640, 430, 121, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDateInput.setFont(font)
        self.labelDateInput.setObjectName("labelDateInput")
        self.labelCarAddingService = QtWidgets.QLabel(Form)
        self.labelCarAddingService.setGeometry(QtCore.QRect(470, 70, 155, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCarAddingService.setFont(font)
        self.labelCarAddingService.setObjectName("labelCarAddingService")
        self.comboBoxForChoseService = QtWidgets.QComboBox(Form)
        self.comboBoxForChoseService.setGeometry(QtCore.QRect(640, 70, 301, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxForChoseService.setFont(font)
        self.comboBoxForChoseService.setObjectName("comboBoxForChoseService")
        self.pushButtonForAddService = QtWidgets.QPushButton(Form)
        self.pushButtonForAddService.setGeometry(QtCore.QRect(730, 110, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonForAddService.setFont(font)
        self.pushButtonForAddService.setObjectName("pushButtonForAddService")
        self.comboBoxForChosingCars = QtWidgets.QComboBox(Form)
        self.comboBoxForChosingCars.setGeometry(QtCore.QRect(115, 70, 241, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxForChosingCars.setFont(font)
        self.comboBoxForChosingCars.setObjectName("comboBoxForChosingCars")
        self.labelCarChose = QtWidgets.QLabel(Form)
        self.labelCarChose.setGeometry(QtCore.QRect(60, 70, 49, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCarChose.setFont(font)
        self.labelCarChose.setObjectName("labelCarChose")
        self.tableWidget_CurentService = QtWidgets.QTableWidget(Form)
        self.tableWidget_CurentService.setGeometry(QtCore.QRect(640, 160, 311, 201))
        self.tableWidget_CurentService.setObjectName("tableWidget_CurentService")
        self.tableWidget_CurentService.setColumnCount(2)
        self.tableWidget_CurentService.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_CurentService.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_CurentService.setHorizontalHeaderItem(1, item)
        self.dateEditForDateInput = QtWidgets.QDateEdit(Form)
        self.dateEditForDateInput.setGeometry(QtCore.QRect(780, 430, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEditForDateInput.setFont(font)
        self.dateEditForDateInput.setObjectName("dateEditForDateInput")
        self.pushButtonDetailedServices = QtWidgets.QPushButton(Form)
        self.pushButtonDetailedServices.setGeometry(QtCore.QRect(230, 530, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonDetailedServices.setFont(font)
        self.pushButtonDetailedServices.setObjectName("pushButtonDetailedServices")
        self.comboBox_ForChoseWorkerToWork = QtWidgets.QComboBox(Form)
        self.comboBox_ForChoseWorkerToWork.setGeometry(QtCore.QRect(970, 70, 301, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_ForChoseWorkerToWork.setFont(font)
        self.comboBox_ForChoseWorkerToWork.setObjectName("comboBox_ForChoseWorkerToWork")
        self.label_ForAddWorkerToWork = QtWidgets.QLabel(Form)
        self.label_ForAddWorkerToWork.setGeometry(QtCore.QRect(1020, 30, 201, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ForAddWorkerToWork.setFont(font)
        self.label_ForAddWorkerToWork.setObjectName("label_ForAddWorkerToWork")
        self.tableWidget_AddWorkerToWork = QtWidgets.QTableWidget(Form)
        self.tableWidget_AddWorkerToWork.setGeometry(QtCore.QRect(970, 160, 361, 251))
        self.tableWidget_AddWorkerToWork.setObjectName("tableWidget_AddWorkerToWork")
        self.tableWidget_AddWorkerToWork.setColumnCount(2)
        self.tableWidget_AddWorkerToWork.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_AddWorkerToWork.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_AddWorkerToWork.setHorizontalHeaderItem(1, item)
        self.pushButton_ForAddWorkerToWork = QtWidgets.QPushButton(Form)
        self.pushButton_ForAddWorkerToWork.setGeometry(QtCore.QRect(1070, 110, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_ForAddWorkerToWork.setFont(font)
        self.pushButton_ForAddWorkerToWork.setObjectName("pushButton_ForAddWorkerToWork")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OrderMakingForm"))
        self.pushButtonForAddOrder.setText(_translate("Form", "Додати замовлення"))
        self.label_main_auto.setText(_translate("Form", "Створення замовлення"))
        item = self.tableWidgetForOutputCars.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Авто"))
        item = self.tableWidgetForOutputCars.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Послги"))
        item = self.tableWidgetForOutputCars.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ціна"))
        item = self.tableWidgetForOutputCars.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Дата"))
        self.labeForPriceCalculate.setText(_translate("Form", "Ціна:"))
        self.labelDateInput.setText(_translate("Form", "Обріть дату:"))
        self.labelCarAddingService.setText(_translate("Form", "Оберіть послуги:"))
        self.pushButtonForAddService.setText(_translate("Form", "Додати"))
        self.labelCarChose.setText(_translate("Form", "Авто:"))
        item = self.tableWidget_CurentService.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Назва"))
        item = self.tableWidget_CurentService.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Ціна"))
        self.pushButtonDetailedServices.setText(_translate("Form", "Робота із замовленями"))
        self.label_ForAddWorkerToWork.setText(_translate("Form", "Обреріть працівників:"))
        item = self.tableWidget_AddWorkerToWork.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ім\'я"))
        item = self.tableWidget_AddWorkerToWork.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Ціна"))
        self.pushButton_ForAddWorkerToWork.setText(_translate("Form", "Додати"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())