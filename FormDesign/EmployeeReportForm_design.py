# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmployeeReportForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1163, 580)
        self.tableWidgetForFreeWorker = QtWidgets.QTableWidget(Form)
        self.tableWidgetForFreeWorker.setGeometry(QtCore.QRect(30, 130, 421, 371))
        self.tableWidgetForFreeWorker.setObjectName("tableWidgetForFreeWorker")
        self.tableWidgetForFreeWorker.setColumnCount(3)
        self.tableWidgetForFreeWorker.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForFreeWorker.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForFreeWorker.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForFreeWorker.setHorizontalHeaderItem(2, item)
        self.label_MainWorkerReport = QtWidgets.QLabel(Form)
        self.label_MainWorkerReport.setGeometry(QtCore.QRect(370, 10, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_MainWorkerReport.setFont(font)
        self.label_MainWorkerReport.setObjectName("label_MainWorkerReport")
        self.label_MainWorkerReport_2 = QtWidgets.QLabel(Form)
        self.label_MainWorkerReport_2.setGeometry(QtCore.QRect(30, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_MainWorkerReport_2.setFont(font)
        self.label_MainWorkerReport_2.setObjectName("label_MainWorkerReport_2")
        self.tableWidgetForBusyWorker = QtWidgets.QTableWidget(Form)
        self.tableWidgetForBusyWorker.setGeometry(QtCore.QRect(470, 130, 421, 371))
        self.tableWidgetForBusyWorker.setObjectName("tableWidgetForBusyWorker")
        self.tableWidgetForBusyWorker.setColumnCount(3)
        self.tableWidgetForBusyWorker.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForBusyWorker.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForBusyWorker.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetForBusyWorker.setHorizontalHeaderItem(2, item)
        self.label_MainWorkerReport_4 = QtWidgets.QLabel(Form)
        self.label_MainWorkerReport_4.setGeometry(QtCore.QRect(470, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_MainWorkerReport_4.setFont(font)
        self.label_MainWorkerReport_4.setObjectName("label_MainWorkerReport_4")
        self.pushButtonForMoveWorkerToFree = QtWidgets.QPushButton(Form)
        self.pushButtonForMoveWorkerToFree.setGeometry(QtCore.QRect(940, 230, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonForMoveWorkerToFree.setFont(font)
        self.pushButtonForMoveWorkerToFree.setObjectName("pushButtonForMoveWorkerToFree")
        self.label_ForMoveToFreeWorker = QtWidgets.QLabel(Form)
        self.label_ForMoveToFreeWorker.setGeometry(QtCore.QRect(920, 151, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ForMoveToFreeWorker.setFont(font)
        self.label_ForMoveToFreeWorker.setObjectName("label_ForMoveToFreeWorker")
        self.comboBoxChoseWorkerForMoveToFree = QtWidgets.QComboBox(Form)
        self.comboBoxChoseWorkerForMoveToFree.setGeometry(QtCore.QRect(950, 180, 161, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxChoseWorkerForMoveToFree.setFont(font)
        self.comboBoxChoseWorkerForMoveToFree.setObjectName("comboBoxChoseWorkerForMoveToFree")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "EmployeeReportForm"))
        item = self.tableWidgetForFreeWorker.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ім\'я"))
        item = self.tableWidgetForFreeWorker.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Посада"))
        item = self.tableWidgetForFreeWorker.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Дохід"))
        self.label_MainWorkerReport.setText(_translate("Form", "Звітність працівників"))
        self.label_MainWorkerReport_2.setText(_translate("Form", "Вільні:"))
        item = self.tableWidgetForBusyWorker.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ім\'я"))
        item = self.tableWidgetForBusyWorker.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Посада"))
        item = self.tableWidgetForBusyWorker.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Дохід"))
        self.label_MainWorkerReport_4.setText(_translate("Form", "Працють:"))
        self.pushButtonForMoveWorkerToFree.setText(_translate("Form", "Відправити"))
        self.label_ForMoveToFreeWorker.setText(_translate("Form", "Відпрвити в стан очікування:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())