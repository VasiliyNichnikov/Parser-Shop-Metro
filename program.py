import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem


class Program(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.window_opened = False
        # self.ui = Ui_MainWindow()

    def load_interface(self) -> None:
        uic.loadUi("static/interface/main.ui", self)
        # self.ui.setupUi(self)
        # self.setWindowTitle("Парсер сайтов")

    def connect_buttons(self) -> None:
        pass
        # button_add_item = self.__add_item_button(ButtonAddItem())
        # button_add_item.button_add.clicked.connect(self.__open_widget_add_site)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    program = Program()
    program.load_interface()
    program.connect_buttons()
    program.show()

    sys.exit(app.exec())
