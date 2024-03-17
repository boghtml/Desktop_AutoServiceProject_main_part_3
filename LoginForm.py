import hashlib

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui

from DataBase_trial.DataBase import check_user_credentials
from FormDesign.LoginForm_design import Ui_Form as Ui_LoginForm

from MainForm import MainForm


class Autorization(QtWidgets.QWidget, Ui_LoginForm):
    def __init__(self, parent=None):
        super(Autorization, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_ToSwithVivibleOfPasword.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: none; /* Видаляємо обведення */
            }

            QPushButton:hover {
                /* Можете залишити цей блок, якщо хочете визначити стиль для наведення курсору */
            }
        """)

        self.label.setStyleSheet(
            "background-image: url(D://Qt_designer//AutoServiseProject//FormDesign//Resources//1662046854_2-kartinkin-net-p-zadnii-fon-dlya-avto-krasivo-2.jpg);\n"
            "\n"
            "background-repeat: no-repeat;\n"
            "background-size: cover;\n"
            "border-top-left-radius: 50px;\n"
            "")

        # Зв'яжіть кнопки і поля з методами
        self.pushButton_ForAplyLogIn.clicked.connect(self.login)

        self.label_LinkToRegistrForm.mousePressEvent = self.open_registration_form

        self.pushButton_ToSwithVivibleOfPasword.clicked.connect(self.toggle_password_visibility)

    def login(self):
        username = self.lineEdit_ForNameInput.text()
        password = self.lineEdit_ForPasswordInput.text()

        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        if not username or not hashed_password:
            QMessageBox.warning(self, "Помилка", "Ім'я користувача та пароль не можуть бути порожніми!")
            return

        if username == "admin" and password == "admin":
            QMessageBox.information(self, "Вхід в систему", "Ви ввійшли як адміністратор.")
            self.open_main_form(is_admin=True)
        elif check_user_credentials(username, hashed_password):
            QMessageBox.information(self, "Вхід в систему", "Ви ввійшли як звичайний користувач.")
            self.open_main_form(is_admin=False)
        else:
            QMessageBox.warning(self, 'Помилка', 'Неправильний логін або пароль!')

    def open_main_form(self, is_admin):
        self.main_form = MainForm(is_admin=is_admin)
        self.main_form.show()
        self.close()

    def open_registration_form(self, event):
        from RegisterForm import Registration  # Імпорт всередині методу
        self.register_form = Registration()
        self.register_form.show()
        self.close()

    def toggle_password_visibility(self):
        if self.lineEdit_ForPasswordInput.echoMode() == QtWidgets.QLineEdit.Password:
            self.lineEdit_ForPasswordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.pushButton_ToSwithVivibleOfPasword.setIcon(
                QtGui.QIcon('D://Qt_designer//AutoServiseProject//FormDesign//Resources//show.png'))
        else:
            self.lineEdit_ForPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.pushButton_ToSwithVivibleOfPasword.setIcon(
                QtGui.QIcon('D://Qt_designer//AutoServiseProject//FormDesign//Resources//hide.png'))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login_form = Autorization()
    login_form.show()
    sys.exit(app.exec_())
