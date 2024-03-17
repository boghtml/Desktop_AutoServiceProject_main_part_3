# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetailedServiceForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1080, 600)
        self.comboBoxForSortOrders = QtWidgets.QComboBox(Form)
        self.comboBoxForSortOrders.setGeometry(QtCore.QRect(90, 91, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxForSortOrders.setFont(font)
        self.comboBoxForSortOrders.setObjectName("comboBoxForSortOrders")
        self.tableWidgetForOutputOrders = QtWidgets.QTableWidget(Form)
        self.tableWidgetForOutputOrders.setGeometry(QtCore.QRect(90, 140, 612, 390))
        self.tableWidgetForOutputOrders.setObjectName("tableWidgetForOutputOrders")
        self.tableWidgetForOutputOrders.setColumnCount(4)
        self.tableWidgetForOutputOrders.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForOutputOrders.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForOutputOrders.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForOutputOrders.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForOutputOrders.setHorizontalHeaderItem(3, item)
        self.labelDataForOutput = QtWidgets.QLabel(Form)
        self.labelDataForOutput.setGeometry(QtCore.QRect(480, 91, 111, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDataForOutput.setFont(font)
        self.labelDataForOutput.setObjectName("labelDataForOutput")
        self.comboBoxForDataOutputOrders = QtWidgets.QComboBox(Form)
        self.comboBoxForDataOutputOrders.setGeometry(QtCore.QRect(590, 91, 221, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxForDataOutputOrders.setFont(font)
        self.comboBoxForDataOutputOrders.setObjectName("comboBoxForDataOutputOrders")
        self.labelDateInput = QtWidgets.QLabel(Form)
        self.labelDateInput.setGeometry(QtCore.QRect(740, 190, 251, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDateInput.setFont(font)
        self.labelDateInput.setObjectName("labelDateInput")
        self.pushButtonForAplyDataQuery = QtWidgets.QPushButton(Form)
        self.pushButtonForAplyDataQuery.setGeometry(QtCore.QRect(820, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonForAplyDataQuery.setFont(font)
        self.pushButtonForAplyDataQuery.setObjectName("pushButtonForAplyDataQuery")
        self.label_main_auto = QtWidgets.QLabel(Form)
        self.label_main_auto.setGeometry(QtCore.QRect(340, 10, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_main_auto.setFont(font)
        self.label_main_auto.setObjectName("label_main_auto")
        self.pushButtonForDeleteOrder = QtWidgets.QPushButton(Form)
        self.pushButtonForDeleteOrder.setGeometry(QtCore.QRect(780, 280, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonForDeleteOrder.setFont(font)
        self.pushButtonForDeleteOrder.setObjectName("pushButtonForDeleteOrder")
        self.pushButton_ForAplySort = QtWidgets.QPushButton(Form)
        self.pushButton_ForAplySort.setGeometry(QtCore.QRect(320, 80, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_ForAplySort.setFont(font)
        self.pushButton_ForAplySort.setObjectName("pushButton_ForAplySort")
        self.comboBoxChosingOrderDelete = QtWidgets.QComboBox(Form)
        self.comboBoxChosingOrderDelete.setGeometry(QtCore.QRect(730, 230, 271, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBoxChosingOrderDelete.setFont(font)
        self.comboBoxChosingOrderDelete.setObjectName("comboBoxChosingOrderDelete")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DetailedServiceForm"))
        item = self.tableWidgetForOutputOrders.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Авто"))
        item = self.tableWidgetForOutputOrders.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Послги"))
        item = self.tableWidgetForOutputOrders.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ціна"))
        item = self.tableWidgetForOutputOrders.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Дата"))
        self.labelDataForOutput.setText(_translate("Form", "Вивести за:"))
        self.labelDateInput.setText(_translate("Form", "Замовлення для видаленя:"))
        self.pushButtonForAplyDataQuery.setText(_translate("Form", "Вивести"))
        self.label_main_auto.setText(_translate("Form", "Робота із замовленнями"))
        self.pushButtonForDeleteOrder.setText(_translate("Form", "Видалити замовлення"))
        self.pushButton_ForAplySort.setText(_translate("Form", "Посортувати"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())