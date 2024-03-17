from PyQt5.QtCore import QObject, pyqtSignal


class Signals(QObject):
    order_updated = pyqtSignal()
    employee_status_changed = pyqtSignal()
    car_added = pyqtSignal()
    employee_added = pyqtSignal()

    services_added = pyqtSignal()


signals = Signals()
