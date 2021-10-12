import sys
from PyQt5 import QtWidgets, uic
from convertor.convertor_json import sterilization, deserialization
from parameters import Parameters
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem


class Program(QMainWindow):
    def __init__(self, parameters: Parameters) -> None:
        super().__init__()
        self.__parameters = parameters

    def load_interface(self) -> None:
        uic.loadUi(self.__parameters.path_interface, self)

    def connect_buttons(self) -> None:
        pass

    def __add_url(self) -> None:
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    path_settings = "static/settings.json"
    settings = deserialization(path_settings)

    program = Program(settings)
    program.load_interface()
    program.connect_buttons()
    program.show()

    sys.exit(app.exec())
