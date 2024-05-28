from PyQt5 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Text Area Example')

        self.text_area = QtWidgets.QTextEdit(self)
        self.text_area.setGeometry(20, 20, 400, 300)

        self.submit_button = QtWidgets.QPushButton('Submit', self)
        self.submit_button.setGeometry(20, 330, 80, 30)
        self.submit_button.clicked.connect(self.on_submit)

    def on_submit(self):
        comment = self.text_area.toPlainText()
        print('User Comment:', comment)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
