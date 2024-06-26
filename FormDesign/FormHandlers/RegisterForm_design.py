# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewRegisterForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(590, 480)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 10, 590, 480))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
                                  "    color:rgba(255, 255, 255, 210);\n"
                                  "    border-radius:5px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#pushButton:hover{\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#pushButton:pressed{\n"
                                  "    padding-left:5px;\n"
                                  "    padding-top:5px;\n"
                                  "    background-color:rgba(150, 123, 111, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
                                  "    background-color: rgba(0, 0, 0, 0);\n"
                                  "    color:rgba(85, 98, 112, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
                                  "    color: rgba(131, 96, 53, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
                                  "    padding-left:5px;\n"
                                  "    padding-top:5px;\n"
                                  "    color:rgba(91, 88, 53, 255);\n"
                                  "}\n"
                                  "\n"
                                  "")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(29, 30, 291, 430))
        self.label.setStyleSheet(
            "background-image: url(:/Images/D:/Qt_designer/AutoServiseProject/FormDesign/Resources/1662046854_2-kartinkin-net-p-zadnii-fon-dlya-avto-krasivo-2.jpg);\n"
            "\n"
            "background-repeat: no-repeat;\n"
            "background-size: cover;\n"
            "border-top-left-radius: 50px;\n"
            "")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
                                   "background-image: url(:/Images/koons-automotive-VKAD70LvKEg-unsplash.jpg);\n"
                                   "border-top-left-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 291, 430))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
                                   "border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(300, 60, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_ForNewNameInput = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_ForNewNameInput.setGeometry(QtCore.QRect(300, 160, 211, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_ForNewNameInput.setFont(font)
        self.lineEdit_ForNewNameInput.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                                    "border:none;\n"
                                                    "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                                    "color:rgba(0, 0, 0, 240);\n"
                                                    "padding-bottom:7px;")
        self.lineEdit_ForNewNameInput.setText("")
        self.lineEdit_ForNewNameInput.setObjectName("lineEdit_ForNewNameInput")
        self.lineEdit__ForNewPasswordInput = QtWidgets.QLineEdit(self.widget)
        self.lineEdit__ForNewPasswordInput.setGeometry(QtCore.QRect(300, 220, 211, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit__ForNewPasswordInput.setFont(font)
        self.lineEdit__ForNewPasswordInput.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                                         "border:none;\n"
                                                         "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                                         "color:rgba(0, 0, 0, 240);\n"
                                                         "padding-bottom:7px;")
        self.lineEdit__ForNewPasswordInput.setText("")
        self.lineEdit__ForNewPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit__ForNewPasswordInput.setObjectName("lineEdit__ForNewPasswordInput")
        self.pushButton_ForAplyRegistr = QtWidgets.QPushButton(self.widget)
        self.pushButton_ForAplyRegistr.setGeometry(QtCore.QRect(300, 300, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ForAplyRegistr.setFont(font)
        self.pushButton_ForAplyRegistr.setStyleSheet("QPushButton {\n"
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
        self.pushButton_ForAplyRegistr.setObjectName("pushButton_ForAplyRegistr")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 360, 141, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 80, 230, 131))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 75);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(40, 140, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.pushButton_ToSwithVivibleOfPasword = QtWidgets.QPushButton(self.widget)
        self.pushButton_ToSwithVivibleOfPasword.setGeometry(QtCore.QRect(510, 220, 31, 31))
        self.pushButton_ToSwithVivibleOfPasword.setStyleSheet("border-image: url(:/Images/hide.png);")
        self.pushButton_ToSwithVivibleOfPasword.setText("")
        self.pushButton_ToSwithVivibleOfPasword.setObjectName("pushButton_ToSwithVivibleOfPasword")
        self.pushButton_ForBackToLiginForm = QtWidgets.QPushButton(self.widget)
        self.pushButton_ForBackToLiginForm.setGeometry(QtCore.QRect(70, 400, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_ForBackToLiginForm.setFont(font)
        self.pushButton_ForBackToLiginForm.setStyleSheet("QPushButton {\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(144, 238, 144); /* Світло зелена */\n"
                                                         "    border-radius: 10px;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QPushButton:hover {\n"
                                                         "    background-color: rgb(34, 139, 34); /* Темно зелена при наведенні */\n"
                                                         "}\n"
                                                         "")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("D:/Qt_designer/AutoServiseProject/FormDesign/Resources/free-icon-left-arrow-271218.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ForBackToLiginForm.setIcon(icon)
        self.pushButton_ForBackToLiginForm.setObjectName("pushButton_ForBackToLiginForm")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(40, 90, 231, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit_ForNewNameInput.raise_()
        self.lineEdit__ForNewPasswordInput.raise_()
        self.pushButton_ForAplyRegistr.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_6.raise_()
        self.label_8.raise_()
        self.pushButton_ToSwithVivibleOfPasword.raise_()
        self.pushButton_ForBackToLiginForm.raise_()
        self.label_7.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RegisterForm"))
        self.label_4.setText(_translate("Form", "Реєстрація"))
        self.lineEdit_ForNewNameInput.setPlaceholderText(_translate("Form", " Логін"))
        self.lineEdit__ForNewPasswordInput.setPlaceholderText(_translate("Form", " Пароль"))
        self.pushButton_ForAplyRegistr.setText(_translate("Form", "Створити акаут"))
        self.pushButton_2.setText(_translate("Form", "E"))
        self.pushButton_3.setText(_translate("Form", "D"))
        self.pushButton_4.setText(_translate("Form", "M"))
        self.pushButton_5.setText(_translate("Form", "C"))
        self.label_8.setText(_translate("Form", "Ласкаво просимо в Auto Service \n"
                                                "Ваше найкраще рішення для догляду за авто!"))
        self.pushButton_ForBackToLiginForm.setText(_translate("Form", "Авторизація"))
        self.label_7.setText(_translate("Form", "AutoService"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
