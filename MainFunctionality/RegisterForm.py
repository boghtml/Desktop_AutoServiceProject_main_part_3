from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from DataBase.DataBase import add_user_base, is_username_available
from FormDesign.FormHandlers.RegisterForm_design import Ui_Form as Ui_RegisterForm
from MainFunctionality.LoginForm import Autorization


class Registration(QtWidgets.QWidget, Ui_RegisterForm):
    def __init__(self, parent=None):
        super(Registration, self).__init__(parent)
        self.setupUi(self)

        self.initializeUI()

        self.pushButton_ToSwithVivibleOfPasword.setStyleSheet("""
                    QPushButton {
                        background-color: white;
                        border: none; /* Видаляємо обведення */
                    }

                    QPushButton:hover {
                        /* Можете залишити цей блок, якщо хочете визначити стиль для наведення курсору */
                    }
                """)
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
                                   "background-image: url(:/Images/koons-automotive-VKAD70LvKEg-unsplash.jpg);\n"
                                   "border-top-left-radius: 50px;")

        self.label.setStyleSheet(
            "background-image: url(D://Qt_designer//AutoServiseProject//FormDesign//Resources//1662046854_2-kartinkin-net-p-zadnii-fon-dlya-avto-krasivo-2.jpg);\n"
            "\n"
            "background-repeat: no-repeat;\n"
            "background-size: cover;\n"
            "border-top-left-radius: 50px;\n"
            "")

        self.pushButton_ToSwithVivibleOfPasword.setIcon(
            QtGui.QIcon('D:/Qt_designer/AutoServiseProject/FormDesign/Resources/hide.png'))
        # Зв'яжіть кнопки і поля з методами
        self.pushButton_ForAplyRegistr.clicked.connect(self.register)

        self.pushButton_ForBackToLiginForm.clicked.connect(self.open_login_form)

        self.pushButton_ToSwithVivibleOfPasword.clicked.connect(self.toggle_password_visibility)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.register()
        super(Registration, self).keyPressEvent(event)

    def register(self):
        new_username = self.lineEdit_ForNewNameInput.text()
        new_password = self.lineEdit__ForNewPasswordInput.text()

        if not new_username or not new_password:
            QMessageBox.warning(self, "Помилка", "Ім'я користувача та пароль не можуть бути порожніми!")
            return

        if is_username_available(new_username):
            user_data = {
                "username": new_username,
                "password": new_password  # У реальному додатку пароль потрібно хешувати!
            }

            try:
                user_id = add_user_base(new_username, new_password)
                QtWidgets.QMessageBox.information(self, "Успіх", "Користувач успішно зареєстрований.")
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Помилка", "Не вдалося зареєструвати користувача.")
                print(e)

            self.login_form = Autorization()
            self.login_form.show()
            self.close()

        else:
            QMessageBox.warning(self, "Помилка", "Користувач з таким ім'ям вже існує.")

        self.lineEdit_ForNewNameInput.clear()
        self.lineEdit__ForNewPasswordInput.clear()

    def open_login_form(self):
        from MainFunctionality.LoginForm import Autorization  # Імпорт всередині методу
        self.login_form = Autorization()
        self.login_form.show()
        self.close()

    def toggle_password_visibility(self):
        if self.lineEdit__ForNewPasswordInput.echoMode() == QtWidgets.QLineEdit.Password:
            self.lineEdit__ForNewPasswordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.pushButton_ToSwithVivibleOfPasword.setIcon(
                QtGui.QIcon('D:/Qt_designer/AutoServiseProject/FormDesign/Resources/show.png'))
        else:
            self.lineEdit__ForNewPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.pushButton_ToSwithVivibleOfPasword.setIcon(
                QtGui.QIcon('D:/Qt_designer/AutoServiseProject/FormDesign/Resources/hide.png'))

    def initializeUI(self):
        self.pushButton_ForAplyRegistr.setToolTip("Натисніть, щоб зареєструватися")
        self.pushButton_2.setToolTip("Посилання на Facebook")
        self.pushButton_3.setToolTip("Посилання на Instagram")
        self.pushButton_4.setToolTip("Посилання на Twitter")
        self.pushButton_5.setToolTip("Посилання на Telegram")
        self.pushButton_ToSwithVivibleOfPasword.setToolTip("Натисніть, щоб показати/приховати пароль")
        self.pushButton_ForBackToLiginForm.setToolTip("Натисніть, щоб перейти до форми авторизації")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    register_form = Registration()
    register_form.show()
    sys.exit(app.exec_())
