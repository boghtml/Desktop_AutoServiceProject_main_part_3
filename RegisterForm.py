from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui

from FormDesign.RegisterForm_design import Ui_Form as Ui_RegisterForm
from DataBase_trial.DataBase import add_user_base, is_username_available

from LoginForm import Autorization


class Registration(QtWidgets.QWidget, Ui_RegisterForm):
    def __init__(self, parent=None):
        super(Registration, self).__init__(parent)
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
        # Зв'яжіть кнопки і поля з методами
        self.pushButton_ForAplyRegistr.clicked.connect(self.register)

        self.pushButton_ForBackToLiginForm.clicked.connect(self.open_login_form)

        self.pushButton_ToSwithVivibleOfPasword.clicked.connect(self.toggle_password_visibility)

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
        from LoginForm import Autorization  # Імпорт всередині методу
        self.login_form = Autorization()
        self.login_form.show()
        self.close()

    def toggle_password_visibility(self):
        if self.lineEdit__ForNewPasswordInput.echoMode() == QtWidgets.QLineEdit.Password:
            self.lineEdit__ForNewPasswordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.pushButton_ToSwithVivibleOfPasword.setIcon(
                QtGui.QIcon('D://Qt_designer//AutoServiseProject//FormDesign//Resources//show.png'))
        else:
            self.lineEdit__ForNewPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.pushButton_ToSwithVivibleOfPasword.setIcon(
                QtGui.QIcon('D://Qt_designer//AutoServiseProject//FormDesign//Resources//hide.png'))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    register_form = Registration()
    register_form.show()
    sys.exit(app.exec_())
